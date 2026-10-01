"""Live transcription of Windows system/speaker audio.

Captures the default Windows speaker through WASAPI loopback and transcribes
short chunks with faster-whisper.

Stop with Ctrl+C.
"""


from __future__ import annotations
import warnings
from soundcard.mediafoundation import SoundcardRuntimeWarning

warnings.filterwarnings("ignore", category=SoundcardRuntimeWarning)

from datetime import datetime
from pathlib import Path
import sys

import numpy as np
import soundcard as sc
from faster_whisper import WhisperModel

SAMPLE_RATE = 16_000
CHUNK_SECONDS = 3.0
MODEL_SIZE = "base.en"  # Try "tiny.en" for lower latency, "small.en" for accuracy.
OUTPUT_FILE = Path("system_audio_transcript.txt")


def find_loopback_device():
    """Return the loopback microphone corresponding to the default speaker."""
    speaker = sc.default_speaker()
    loopbacks = [
        mic
        for mic in sc.all_microphones(include_loopback=True)
        if getattr(mic, "isloopback", False)
    ]

    if not loopbacks:
        raise RuntimeError(
            "No Windows loopback recording device was found. "
            "Make sure an output/speaker device is enabled."
        )

    speaker_name = speaker.name.lower()
    for mic in loopbacks:
        mic_name = mic.name.lower()
        if speaker_name in mic_name or mic_name in speaker_name:
            return speaker, mic

    # Usually there is only one relevant loopback device. Fall back to the first.
    return speaker, loopbacks[0]


def main() -> None:
    print("Loading Whisper model...", flush=True)
    model = WhisperModel(
        MODEL_SIZE,
        device="cpu",
        compute_type="int8",
        cpu_threads=4,
    )

    try:
        speaker, loopback = find_loopback_device()
    except Exception as exc:
        print(f"Audio device error: {exc}", file=sys.stderr)
        print("\nAvailable loopback devices:", file=sys.stderr)
        for mic in sc.all_microphones(include_loopback=True):
            if getattr(mic, "isloopback", False):
                print(f"  - {mic.name}", file=sys.stderr)
        raise SystemExit(1)

    print(f"Listening to system audio: {speaker.name}")
    print(f"Loopback device: {loopback.name}")
    print(f"Transcript file: {OUTPUT_FILE.resolve()}")
    print("Press Ctrl+C to stop.\n")

    num_frames = int(SAMPLE_RATE * CHUNK_SECONDS)

    with OUTPUT_FILE.open("a", encoding="utf-8") as out:
        out.write(f"\n\n--- Session {datetime.now().isoformat(timespec='seconds')} ---\n")
        out.flush()

        try:
            with loopback.recorder(samplerate=SAMPLE_RATE, channels=1) as recorder:
                while True:
                    audio = recorder.record(numframes=num_frames)
                    audio = np.asarray(audio[:, 0], dtype=np.float32)

                    # Ignore nearly silent chunks to avoid unnecessary inference.
                    if audio.size == 0 or float(np.max(np.abs(audio))) < 0.003:
                        continue

                    segments, _ = model.transcribe(
                        audio,
                        language="en",
                        beam_size=1,
                        vad_filter=True,
                        condition_on_previous_text=False,
                    )

                    text = " ".join(seg.text.strip() for seg in segments).strip()
                    if not text:
                        continue

                    print(text, flush=True)
                    out.write(text + "\n")
                    out.flush()

        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
