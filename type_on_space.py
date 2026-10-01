"""Type clipboard text into whichever app is focused after Space is pressed.

Workflow:
1. Copy the text you want typed to the clipboard.
2. Run this script.
3. Click into any text field/editor.
4. Press Space once.
5. The trigger Space is suppressed and the text is typed at about 75 WPM.
"""

from __future__ import annotations

import random
import time

import pyperclip
from pynput import keyboard

WPM = 75
CHARS_PER_WORD = 5
BASE_DELAY = 60.0 / (WPM * CHARS_PER_WORD)  # ~0.16 sec/character at 75 WPM
JITTER_LOW = 0.75
JITTER_HIGH = 1.25


def wait_for_space() -> None:
    """Wait for one global Space press and suppress that trigger keystroke."""
    def on_press(key):
        if key == keyboard.Key.space:
            return False  # Stops the listener; with suppress=True, Space is not sent to the app.
        return None

    with keyboard.Listener(on_press=on_press, suppress=True) as listener:
        listener.join()


def human_delay(ch: str) -> float:
    """Return a small randomized delay while keeping the long-run speed near WPM."""
    delay = BASE_DELAY * random.uniform(JITTER_LOW, JITTER_HIGH)

    # Humans tend to pause a little more at phrase/sentence boundaries.
    if ch in ",;:":
        delay += random.uniform(0.03, 0.08)
    elif ch in ".!?":
        delay += random.uniform(0.06, 0.14)
    elif ch == "\n":
        delay += random.uniform(0.08, 0.18)

    return delay


def type_text(text: str) -> None:
    controller = keyboard.Controller()

    for ch in text:
        if ch == "\n":
            controller.press(keyboard.Key.enter)
            controller.release(keyboard.Key.enter)
        elif ch == "\t":
            controller.press(keyboard.Key.tab)
            controller.release(keyboard.Key.tab)
        else:
            controller.type(ch)

        time.sleep(human_delay(ch))


def main() -> None:
    text = pyperclip.paste()

    if not text:
        print("Clipboard is empty. Copy some text first, then run the script again.")
        return

    approx_seconds = len(text) * BASE_DELAY
    print(f"Loaded {len(text)} characters from clipboard.")
    print(f"Target speed: about {WPM} WPM (~{approx_seconds:.1f}s before natural pauses).")
    print("Click the place where you want the text typed, then press SPACE once.")

    wait_for_space()

    # Tiny buffer after the listener closes so focus/keyboard state settles.
    time.sleep(0.15)
    type_text(text)
    print("\nFinished typing.")


if __name__ == "__main__":
    main()
