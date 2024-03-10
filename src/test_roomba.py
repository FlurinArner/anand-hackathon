import time
import serial

PORT = 0


def start(ser):
    """start SCI"""
    ser.write(chr(128))

def safe_mode(ser):
    ser.write(chr(131))
    

def vacuum_on(ser):
    ser.write(chr(138))
    ser.write(chr(2))

def vacuum_off(ser):
    ser.write(chr(138))
    ser.write(chr(0))

def light_test(ser):
    """Example: to turn on the dirt detect and spot LEDs, make the status
    LED red, and to light the power LED green at half intensity,
    send the serial byte sequence [139] [25] [0] [128]"""
    ser.write(chr(139))
    ser.write(chr(25))
    ser.write(chr(0))
    ser.write(chr(128))

def beep(ser):
    """In this example we will send Roomba commands that will cause the robot to “beep”.

    128 132 (Press the “Send Numbers” button)
    140 0 1 62 32 (Press the “Send Numbers” button)
    141 0 (Press the “Send Numbers” button)

    """

    ser.write(chr(128))
    ser.write(chr(132))
    ser.write(chr(140))
    ser.write(chr(0))
    ser.write(chr(1))
    ser.write(chr(62))
    ser.write(chr(32))
    ser.write(chr(141))
    ser.write(chr(0))

if __name__ == "__main__":

    ser = serial.Serial(PORT, baudrate=19200,timeout=0.1) # test other baud: 57600
    ser.open()
    # wake up robot
    ser.setRTS (0)
    time.sleep (0.1)
    ser.setRTS (1)
    time.sleep (2)
    # pulse device-detect three times
    for i in range (3):
        ser.setRTS (0)
        time.sleep (0.25)
        ser.setRTS (1)
        time.sleep (0.25)

    # start(ser)
    # safe_mode(ser)
    # vacuum_on(ser)
    # light_test(ser)
    # beep(ser)
    # time.sleep(5)
    # vacuum_off(ser)
    # ser.close()




