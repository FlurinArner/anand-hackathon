from pyjoystick.sdl2 import Key, Joystick, run_event_loop
from . import roomba_control

def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)

def key_received(key):
    if key.keytype == "Button" and key.number == 0:
        roomba_control.drive_forward()
    elif key.keytype == "Button" and key.number == 1:
        roomba_control.turn_right()
    elif key.keytype == "Button" and key.number == 2:
        roomba_control.drive_backward()
    elif key.keytype == "Button" and key.number == 3: 
        roomba_control.turn_left()

roomba_control.init()
run_event_loop(print_add, print_remove, key_received)
