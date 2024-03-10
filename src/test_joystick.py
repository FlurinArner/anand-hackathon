from pyjoystick.sdl2 import Key, Joystick, run_event_loop

def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)

def dictio():
    print("this is the dictionary")
    print("Key.HAT_UP", Key.HAT_UP)
    print("Key.HAT_DOWN", Key.HAT_DOWN)
    print("")
    print("Key.HAT_LEFT", Key.HAT_LEFT)
    print("Key.HAT_UPLEFT", Key.HAT_UPLEFT)
    print("Key.HAT_DOWNLEFT", Key.HAT_DOWNLEFT)
    print("")
    print("Key.HAT_RIGHT", Key.HAT_RIGHT)
    print("Key.HAT_UPRIGHT", Key.HAT_UPRIGHT)
    print("Key.HAT_DOWNRIGHT", Key.HAT_DOWNRIGHT)
    print("----------------------")


def key_received(key):
    print('received', key)
    if key.value == Key.HAT_UP:
        pass
    elif key.value == Key.HAT_DOWN:
        pass
    if key.value == Key.HAT_LEFT:
        pass
    elif key.value == Key.HAT_UPLEFT:
        pass
    elif key.value == Key.HAT_DOWNLEFT:
        pass
    elif key.value == Key.HAT_RIGHT:
        pass
    elif key.value == Key.HAT_UPRIGHT:
        pass
    elif key.value == Key.HAT_DOWNRIGHT:
        pass

dictio()
run_event_loop(print_add, print_remove, key_received)