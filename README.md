# 🛠️ Daily Hacks

### Small Python scripts that make everyday tasks a little easier.

Daily Hacks is my personal collection of simple but useful Python scripts built to automate everyday tasks, save time, and make working on a computer a little more convenient.

The idea behind this repository is pretty straightforward: if something feels repetitive or unnecessarily time-consuming, why not write a small script to handle it?

Some scripts solve minor annoyances, while others explore interesting ways to use Python for automation. Nothing overly complicated, just practical tools that can come in handy.

## 🚀 What's Inside?

### 🖥️ 1. Screen Awake

**File:** `screen_awake_script.py`

Ever had your screen go idle while you're in the middle of something important?

This script helps keep your computer active by automatically pressing the Shift key at random intervals between 30 seconds and 2.5 minutes.

- Simulates periodic keyboard activity.
- Uses randomized intervals instead of a fixed timer.
- Runs quietly in the terminal until you stop it.
- Useful during long-running tasks or processes.

**Run it:**
```bash
python screen_awake_script.py
```

Press `Ctrl+C` to stop.

### 🎙️ 2. System Audio Transcriber

**File:** `system_audio_transcriber.py`

Sometimes it's easier to read something than listen to it again.

This script captures audio playing through your Windows computer and converts spoken English into text using Faster-Whisper.

Whether you're listening to a lecture, watching a video, or reviewing an audio recording, it gives you a convenient way to capture what's being said.

- Captures system audio directly using Windows loopback recording.
- Processes audio in short, 3-second chunks.
- Uses the Whisper speech recognition model.
- Displays recognized speech in the terminal.
- Automatically saves transcripts to `system_audio_transcript.txt`.
- Runs locally using CPU-based transcription.

**Run it:**
```bash
python system_audio_transcriber.py
```

Press `Ctrl+C` when you're done.

*Note: This script captures audio playing on your computer, not directly from your microphone. Transcription accuracy depends on audio quality.*

### ⌨️ 3. Type on Space

**File:** `type_on_space.py`

Copying and pasting is convenient, but sometimes you want text to appear as if it's being typed normally.

This script takes whatever text you've copied and types it character by character into your selected application when you press Space.

It uses small, randomized delays to create a more natural typing pace.

- Reads text directly from your clipboard.
- Starts typing when you press the Space key.
- Types at approximately 75 words per minute by default.
- Adds natural pauses around punctuation and line breaks.
- Works with text fields and editors that accept simulated keyboard input.

**How to use it:**

1. Copy the text you want to type.
2. Run the script.
3. Click the text field where you want it to appear.
4. Press `Space` once to start typing.

```bash
python type_on_space.py
```

The script finishes automatically after typing the copied text.

*Tip: You can adjust the typing speed by changing the `WPM` value in the script.*

## ⚙️ Getting Started

These scripts are written in Python and are primarily intended for Windows systems.

**1. Clone the repository**

```bash
git clone https://github.com/anujkukreti29/Daily-Hacks.git
cd Daily-Hacks
```

**2. Install the required packages**

```bash
pip install -r requirements_audio_and_typing.txt
pip install pyautogui
```

**3. Run whichever script you need**

Each script works independently, so there's no complicated setup or need to run everything together.

For the audio transcriber, the Whisper model may need to be downloaded automatically on its first run.

## 📁 Repository Structure

```text
Daily-Hacks/
│
├── screen_awake_script.py
├── system_audio_transcriber.py
├── system_audio_transcript.txt
├── type_on_space.py
├── requirements_audio_and_typing.txt
└── README.md
```

## 💡 A Few Things to Know

These are lightweight personal utilities, not fully packaged desktop applications. Depending on your system and preferences, you might need to make small adjustments.

The screen-awake script may not override every system's automatic locking policies. The typing script sends actual keyboard input to the focused application, so make sure you've selected the right text field before triggering it.

Also, be mindful of privacy when recording or saving audio transcripts. Only capture audio you're authorized to record.

## 🌱 What's Next?

I plan to keep adding small scripts whenever I come across something worth automating.

There's no fixed roadmap for this repository. It's simply a growing collection of practical ideas, experiments, and little improvements that make everyday computer work easier.

## 🤝 Feedback & Suggestions

If you find something useful, have an idea for another script, or notice something that could be improved, feel free to open an issue or contribute.

I'm always interested in finding simpler and smarter ways to get things done.

---

**Made with Python, curiosity, and a habit of automating the little things.**

[GitHub Profile](https://github.com/anujkukreti29)
