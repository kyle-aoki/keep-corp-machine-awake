# keep-corp-machine-awake

1. Install Python from [python.org](https://python.org)
2. Install dependencies below:

```
// Run with corp. VPN turned off and ADMIN access turned on
pip3 install pyautogui
pip3 install pynput
```

3. Start program:

```
python3 keep-corp-machine-awake.py
```

### How it works

1. Keyboard Listener will wait for 2 mins before turning itself on
2. Executor thread will keep track of the time elapsed since the last action
3. Executor thread will press 'command' if no key presses are detected within 5 minutes
4. When 'command' is pressed, it will prevent your machine from going to sleep
5. When 'command' is pressed, it will trigger the keyboard listener to turn off
6. Keyboard listener will turn on again after two minutes... repeat ad infinitum...

Threads only execute their tasks every 30 seconds in order to keep CPU usage low.
