import pyautogui
import time
from pynput import keyboard
from threading import Thread
import os


class KeepCorpMachineAwake:

    program_start_time = time.time()
    last_action = time.time()
    thread_delay = 30
    listener_min_start_time = 60 * 2
    keyboard_listener = None
    max_inaction_time = 60 * 3
    listening = False

    def handle_status_thread(self):
        print("Program started.")
        print(f"Will update below information every {self.thread_delay} seconds.")

        while True:
            running_for = round(time.time() - self.program_start_time)
            listener_will_start = max(self.listener_min_start_time - self.time_elapsed(), 0)
            will_trigger_key_press_in = max(self.max_inaction_time - self.time_elapsed(), 0)

            print("")
            print(f"  Running for:                   {running_for}")
            print(f"  Time since last key press:     {self.time_elapsed()}")
            print(f"  Listener will start in:        {listener_will_start}")
            print(f"  Listening:                     {self.listening}")
            print(f"  Will trigger key press in:     {will_trigger_key_press_in}")
            print("")

            time.sleep(self.thread_delay)
            os.system('cls' if os.name == 'nt' else 'clear')

    def time_elapsed(self): return round(time.time() - self.last_action)

    def handle_key_pressed(self, key):
        if not self.listening: return
        print(f"Key '{key} pressed.")
        self.last_action = time.time()
        self.listening = False

    def handle_listener_thread(self):
        self.keyboard_listener = keyboard.Listener(on_press=self.handle_key_pressed)
        self.keyboard_listener.start()

        while True:
            time.sleep(self.thread_delay)
            if self.time_elapsed() >= self.listener_min_start_time and not self.listening:
                self.listening = True

    def wake_press(self): pyautogui.press('ctrl')

    def handle_execute_thread(self):
        while True:
            time.sleep(self.thread_delay)
            if self.time_elapsed() >= self.max_inaction_time:
                self.wake_press()

    def start(self):
        listener_thread = Thread(target=self.handle_listener_thread)
        executor_thread = Thread(target=self.handle_execute_thread)
        status_thread = Thread(target=self.handle_status_thread)

        listener_thread.start()
        executor_thread.start()
        status_thread.start()


if __name__ == '__main__':
    main = Thread(target=KeepCorpMachineAwake().start)
    main.start()
