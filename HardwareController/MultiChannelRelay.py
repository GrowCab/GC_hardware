
from time import sleep
from HardwareController.I2C_tools import I2C

from smbus2 import smbus2, i2c_msg
from HardwareController.Hardware import Measurement

class SeedMultiChannelRelay(I2C):
    #Based on the code from:
    #https://github.com/Seeed-Studio/Multi_Channel_Relay_Arduino_Library/
    CHANNLE1_BIT          =  int("0x01", 16)
    CHANNLE2_BIT          =  int("0x02", 16)
    CHANNLE3_BIT          =  int("0x04", 16)
    CHANNLE4_BIT          =  int("0x08", 16)
    CHANNLE5_BIT          =  int("0x10", 16)
    CHANNLE6_BIT          =  int("0x20", 16)
    CHANNLE7_BIT          =  int("0x40", 16)
    CHANNLE8_BIT          =  int("0x80", 16)
    CMD_CHANNEL_CTRL      =	 int("0x10", 16)
    CMD_SAVE_I2C_ADD      =	 int("0x11", 16)
    CMD_READ_I2C_ADD      =	 int("0x12", 16)
    CMD_READ_FIRMWARE_VER =  int("0x13", 16)

    def __init__(self, port=1, address=0x11) -> None:
        self.setup(address=address, port=port)
        self.channel_state = 0

    def calibrate(self):
        pass

    def measure(self, unit) -> Measurement:
        return None
    
    def measures(self) -> str:
        return []

    def getFirmwareVersion(self):
        self.bus.write_byte_data(self.address, self.CMD_READ_FIRMWARE_VER)
        msg = []
        byte = 1
        while byte:
            byte = self.bus.read(self.address, 0)
            print(byte)
            msg.append(byte)
        return msg

    def update_status(self):
        data = [self.CMD_CHANNEL_CTRL, self.channel_state]
        msg = i2c_msg.write(self.address, data)
        self.bus.i2c_rdwr(msg)
        #self.bus.write_i2c_block_data(self.address, 0, data)
        # sleep(0.01)
        # r2 = self.bus.write_byte(self.address, self.channel_state)
        # print(f"Returns.. {r1} {r2}")

    def turn_on_channel(self, channel):
        self.channel_state |= (1 << (channel - 1))
        self.update_status()

    def turn_off_channel(self, channel):
        self.channel_state &= ~(1 << (channel - 1))
        self.update_status()



if __name__ == '__main__':
    smcr = SeedMultiChannelRelay(port=1, address=0x11)
    while(True):
        for i in range(1,5):
            smcr.turn_on_channel(i)
            bin_n = bin(smcr.channel_state)
            print(f'Chnnel state: {bin_n}' )
            sleep(1)
        for i in range(1,5):
            smcr.turn_off_channel(i)
            bin_n = bin(smcr.channel_state)
            print(f'Chnnel state: {bin_n}' )
            sleep(1)
       
        #smcr.getFirmwareVersion()
