from HardwareController.MultiChannelRelay import SeedMultiChannelRelay
from HardwareController.SCD30 import SCD30
from time import sleep
from smbus2 import SMBus

if __name__ == '__main__':
    port = 1
    bus = SMBus(port)
    scd30 = SCD30(bus=bus)
    smcr = SeedMultiChannelRelay(bus=bus, address=0x11)
    j = 0
    while j < 5:
        for m in scd30.measures():
            print(scd30.measure(m))
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
        
        sleep(1)
        j += 1