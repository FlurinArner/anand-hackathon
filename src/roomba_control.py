import time
import serial

class Roomba:
    """
    Roomba class to control the robot vacuum cleaner.
    
    Simple wrapper of the serial class, with human readable functions
    
    """
    def __init__(self):
        ser = serial.Serial(
            port='/dev/ttyS0',
            baudrate=19200, # test other baud: 57600
            timeout=0.1
            ) 
        
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

        self = ser

    def close(self):
        self.close()

    def start(self):
        """start SCI (set roomba in passive mode)"""
        self.write(chr(128).encode())

    def start_cleaning(self):
        """start normal cleaning cycle"""
        self.write(chr(135).encode())

    def safe_mode(self):
        self.write(chr(131).encode())    

    def vacuum_on(self):
        self.write(chr(138).encode())
        self.write(chr(2).encode())

    def vacuum_off(self):
        self.write(chr(138).encode())
        self.write(chr(0).encode())

    def light_test(self):
        """Example: to turn on the dirt detect and spot LEDs, make the status
        LED red, and to light the power LED green at half intensity,
        send the serial byte sequence [139] [25] [0] [128]"""
        self.write(chr(139).encode())
        self.write(chr(25).encode())
        self.write(chr(0).encode())
        self.write(chr(128).encode())

    def beep(self):
        """In this example we will send Roomba commands that will cause the robot to “beep”.

        128 132 (Press the “Send Numbers” button)
        140 0 1 62 32 (Press the “Send Numbers” button)
        141 0 (Press the “Send Numbers” button)

        """

        self.write(chr(128).encode())
        self.write(chr(132).encode())
        self.write(chr(140).encode())
        self.write(chr(0).encode())
        self.write(chr(1).encode())
        self.write(chr(62).encode())
        self.write(chr(32).encode())
        self.write(chr(141).encode())
        self.write(chr(0).encode())

    def drive_forward(self):
        """
        128 131 (Press the “Send Numbers” button)
        137 0 100 128 0 (Press the “Send Numbers” button)
        """
        self.write(chr(128).encode())
        self.write(chr(131).encode())
        self.write(chr(137).encode())
        self.write(chr(0).encode())
        self.write(chr(100).encode())
        self.write(chr(128).encode())
        self.write(chr(0).encode())

    def drive_backward(self):
        """
        128 131 (Press the “Send Numbers” button)
        137 255 156 128 0 (Press the “Send Numbers” button)
        """
        self.write(chr(128).encode())
        self.write(chr(131).encode())
        self.write(chr(137).encode())
        self.write(chr(255).encode())
        self.write(chr(156).encode())
        self.write(chr(128).encode())
        self.write(chr(0).encode())

    def turn_right(self):
        """
        128 131 (Press the “Send Numbers” button)
        137 0 100 255 255 (Press the “Send Numbers” button)
        """
        self.write(chr(128).encode())
        self.write(chr(131).encode())
        self.write(chr(137).encode())
        self.write(chr(0).encode())
        self.write(chr(100).encode())
        self.write(chr(255).encode())
        self.write(chr(255).encode())

    def turn_left(self):
        """
        128 131 (Press the “Send Numbers” button)
        137 0 100 0 1 (Press the “Send Numbers” button)
        """
        self.write(chr(128).encode())
        self.write(chr(131).encode())
        self.write(chr(137).encode())
        self.write(chr(0).encode())
        self.write(chr(100).encode())
        self.write(chr(0).encode())
        self.write(chr(1).encode())

if __name__ == "__main__":

    roomba = Roomba.init()
    print(roomba.ser)

    roomba.start()
    roomba.start_cleaning()
    # roomba.safe_mode()
    # roomba.vacuum_on()
    # roomba.light_test()
    # roomba.beep()
    time.sleep(5)
    # roomba.vacuum_off()
    roomba.close()




