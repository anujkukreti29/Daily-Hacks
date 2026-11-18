import pyautogui
import time
import random

pyautogui.FAILSAFE = True

print("Screen awake script running... Press Ctrl+C to stop.")
print("Keeping your screen alive while your LLM thinks!\n")

try:
    while True:
        # Random delay between 30s and 2.5 minutes
        delay = random.uniform(30, 150)
        print(f"Next Shift press in {delay:.0f} seconds...")
        time.sleep(delay)

        # --- GUARANTEED: Shift key press ---
        pyautogui.press("shift")
        print("  -> Shift pressed")

        # # --- COMPLEMENTARY: Small mouse movement (always happens too) ---
        # x = random.randint(-15, 15)
        # y = random.randint(-15, 15)
        # pyautogui.moveRel(x, y, duration=random.uniform(0.3, 0.8))
        # print(f"  -> Mouse nudged by ({x}, {y})")

        # # --- OCCASIONAL BONUS: Scroll (30% chance) ---
        # if random.random() < 0.3:
        #     pyautogui.scroll(random.choice([1, -1]))
        #     print("  -> Scrolled slightly")

        print()

except KeyboardInterrupt:
    print("\nStopped. Hope your model is done thinking!")