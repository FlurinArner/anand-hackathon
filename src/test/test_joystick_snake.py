from pyjoystick.sdl2 import Key, Joystick, run_event_loop

def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)

def key_received(key):
    if key.keytype == "Button" and key.number == 1:
        print("  #")
    elif key.keytype == "Button" and key.number == 3: 
        print("#  ")
    else:
        print(" # ")

run_event_loop(print_add, print_remove, key_received)
