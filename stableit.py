import pyautogui
import time
from pynput import mouse
from pynput import keyboard

listening = False
last_action = time.time()
pyautogui.FAILSAFE = False

def record_event(*args):
    global listening
    global last_action
    last_action = time.time()
    print('Stopping listener')
    ml.stop()
    kl.stop()
    listening = False


print('program started')

while True:
    if not listening:
        time.sleep(30)
        print('Starting listener')
        listening = True
        ml = mouse.Listener(on_move=record_event, on_click=record_event, on_scroll=record_event)
        kl = keyboard.Listener(on_press=record_event)
        ml.start()
        kl.start()
    while listening:
        elapsed = time.time() - last_action
        print(str(round(elapsed, 0)) + ' seconds elapsed')
        if elapsed > 5: pyautogui.press('ctrl')
        time.sleep(30)
