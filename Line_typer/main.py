import keyboard
import time
time.sleep(3.4)
with open('TEXT.txt') as f:
    for line in f:
        keyboard.write(line)
        time.sleep(1)