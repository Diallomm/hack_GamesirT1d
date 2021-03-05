from bluepy.btle import Peripheral

class T1D:
    _previous_state = ""
    rstick = ''
    def __init__(self, mac_address):
        self._controller = Peripheral(mac_address, 'random')
        self._state_characteristic = self._controller.getCharacteristics(uuid="00008651-0000-1000-8000-00805f9b34fb")[0]
        self.get_state()
        print("Connected")

    def get_state(self) -> bool:
        # Returns True is state did change
        self._state_vec = self._state_characteristic.read()
        if self._state_vec[0] == 0xc9: # Creates garbage values
            return False
        if self._previous_state != self._state_vec:
            self._previous_state = self._state_vec
            self.parse_state()
            return True
        return False
        
    def parse_state(self):
        # Notes: Last byte (data[19] is updated on every controller change - can be used as trigger instead of polling)
        data = self._state_vec

        self.L1 = int(bool(data[9] & 0x40))
        self.L2 = int(data[7]) # int 0-255
        self.R1 = int(bool(data[9] & 0x80))
        self.R2 = int(data[8])

        self.X = int(bool(data[9] & 0x08))
        self.Y = int(bool(data[9] & 0x10))
        self.A = int(bool(data[9] & 0x01))
        self.B = int(bool(data[9] & 0x02))
        self.C1 = int(bool(data[10] & 0x04))
        self.C2 = int(bool(data[10] & 0x08))
        self.MENU = int(bool(data[9] & 0x04))

        self.Down = int(bool(data[11] == 0x05))
        self.Up   = int(bool(data[11] == 0x01))
        self.Left = int(bool(data[11] == 0x07))
        self.Right= int(bool(data[11] == 0x03))

        self.LX = int((data[2] << 2) + ((data[3] & 0xc) >> 2))
        self.LY = int(((data[3] & 0x3f) << 4) + (data[4]>>4))
        self.RX = int(((data[4] & 0xf) << 6) + ((data[5] & 0xc) >> 2) )
        self.RY = int(((data[5] & 0x3) << 8) + ((data[6])))

    def __str__(self):
        return "L1: {}\nL2: {}\nR1: {}\nR2: {}\nX : {}\nY : {}\nA : {}\nB : {}\nC1: {}\nC2: {}\nMENU:  {}\nDown:  {}\nUp:    {}\nLeft:  {}\nRight: {}\nLX : {}\nLY : {}\nRX : {}\nRY : {}".format(
                self.L1, self.L2, self.R1, self.R2, self.X, self.Y, self.A, self.B, self.C1, self.C2, self.MENU, self.Down, self.Up, self.Left, self.Right, self.LX, self.LY, self.RX, self.RY
                )

if __name__ == "__main__":
    controller = T1D('C6:86:A1:05:42:54')
    while 1:
        if controller.get_state():
            print(controller)