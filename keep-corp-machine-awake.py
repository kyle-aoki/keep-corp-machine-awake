import pyautogui
import time
from pynput import keyboard
from threading import Thread


last_action = time.time()
thread_delay = 29
listener_min_start_time = 60 * 2
keyboard_listener = None
max_inaction_time = 60 * 5
listening = False


def handle_status_thread():
    global listening
    while True:
        time.sleep(thread_delay)
        print(f" --> Listening: {listening}, Time Elapsed: {round(time_elapsed())} ")


def time_elapsed():
    global last_action
    return time.time() - last_action


def handle_key_pressed(key):
    global last_action
    global listening
    last_action = time.time()
    keyboard_listener.stop()
    listening = False


def start_keyboard_listener():
    global keyboard_listener
    global listening
    keyboard_listener = keyboard.Listener(on_press=handle_key_pressed)
    keyboard_listener.start()
    listening = True


def handle_listener_thread():
    global thread_delay
    global listener_min_start_time
    global listening
    while True:
        time.sleep(thread_delay)
        if time_elapsed() > listener_min_start_time and not listening:
            start_keyboard_listener()


def wake_press():
    global last_action
    pyautogui.press('command')
    last_action = time.time()


def handle_execute_thread():
    global max_inaction_time
    while True:
        time.sleep(thread_delay)
        if time_elapsed() > max_inaction_time:
            wake_press()
            

listener_thread = Thread(target=handle_listener_thread)
executor_thread = Thread(target=handle_execute_thread)
status_thread = Thread(target=handle_status_thread)

listener_thread.start()
executor_thread.start()
status_thread.start()
