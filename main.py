from pynput import keyboard
import time
import threading

# Флаг для управления потоком
w_pressed = False

def on_press(key):
    global w_pressed
    try:
        if key.char == 'w' and not w_pressed:
            w_pressed = True
            # Запускаем поток для эмуляции нажатий
            threading.Thread(target=press_w_repeatedly).start()
    except AttributeError:
        pass

def on_release(key):
    global w_pressed
    try:
        if key.char == 'w':
            w_pressed = False
    except AttributeError:
        pass

def press_w_repeatedly():
    keyboard_controller = keyboard.Controller()
    while w_pressed:
        keyboard_controller.press('w')
        keyboard_controller.release('w')
        time.sleep(0.001)  # регулируйте интервал для скорости нажатий

# Слушаем клавиатуру
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()