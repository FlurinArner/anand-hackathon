from pyjoystick.sdl2 import Key, Joystick, run_event_loop
from .roomba_control import Roomba


def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)

def func_key_received(roomba):
    def key_received(key):
        if key.keytype == "Button" and key.number == 0:
            roomba.drive_forward()
        elif key.keytype == "Button" and key.number == 1:
            roomba.turn_right()
        elif key.keytype == "Button" and key.number == 2:
            roomba.drive_backward()
        elif key.keytype == "Button" and key.number == 3: 
            roomba.turn_left()
    return key_received

roomba = Roomba.init()
key_received = func_key_received(roomba)
run_event_loop(print_add, print_remove, key_received)
