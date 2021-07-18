import datetime
from HardwareController.Hardware import Measurement
from HardwareController.I2C_tools import I2C
from datetime import datetime, timedelta
import logging
import smbus2
import struct
import time
from smbus2 import SMBus
from smbus2.smbus2 import i2c_msg

#Based on the code from: https://github.com/RequestForCoffee/scd30

def interpret_as_float(integer: int):
    return struct.unpack('!f', struct.pack('!I', integer))[0]

class SCD30(I2C):
    """Python I2C driver for the SCD30 CO2 sensor."""

    def __init__(self, address=0x61,  interval=2, bus=None):
        self.interval = interval
        self.last_sensor_meassure   = None
        self.last_sensor_timestamp  = None
        self.setup(address=address, bus=bus)
        #self.address = 0x61
        #self._i2c = smbus2.SMBus(1)
        
        

    def calibrate(self):
        self.set_measurement_interval(2)
        self.sensor_measure()
        
    def sensor_measure(self):
        #print(f"Last timestamp: {self.last_sensor_timestamp}")
        current_time = datetime.now()
        if self.last_sensor_timestamp != None:
            diff_time = (current_time - self.last_sensor_timestamp).total_seconds()
            #print(f"Diff: {diff_time}")
        else:
            diff_time = 0

        if diff_time > self.interval:
            self.last_sensor_meassure = None  
        
        if self.last_sensor_meassure != None:
            return


        #self.last_sensor_meassure =
        #  None
        self.start_periodic_measurement()
        while self.last_sensor_meassure == None:
            if self.get_data_ready():
                self.last_sensor_meassure  = self.read_measurement()
                self.last_sensor_timestamp = datetime.now()
            else:
                time.sleep(0.2)
        self.stop_periodic_measurement()


    def measure(self, unit) -> Measurement:
        self.sensor_measure()
        # if self.get_data_ready():
        #     self.last_sensor_meassure  = self.read_measurement()
        #     self.last_sensor_timestamp = datetime.now()
        measurement = Measurement()
        measurement.type = unit
        measurement.timestamp = self.last_sensor_timestamp
        #print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
        if measurement.type == "temperature":
            measurement.value = self.last_sensor_meassure[1]
            measurement.unit  = "C"
        elif measurement.type == "humidity":
            measurement.unit  = "%"
            measurement.value = self.last_sensor_meassure[2]
        elif measurement.type == "CO2":
            measurement.unit  = "ppm"
            measurement.value = self.last_sensor_meassure[0]
        else:
            raise NotImplementedError
        return measurement
    
    def measures(self) -> str:
        return ["temperature", "humidity", "CO2"]



    def _pretty_hex(self, data):
        """Formats an I2C message in an easily readable format.
        Parameters:
            data: either None, int, or a list of ints.
        Returns:
            a string '<none>' or hex-formatted data (singular or list).
        """
        if data is None:
            return "<none>"
        if type(data) is int:
            data = [data]
        if len(data) == 0:
            return "<none>"

        if len(data) == 1:
            value = "{:02x}".format(data[0])
            if len(value) % 2:
                value = "0" + value
            return "0x" + value
        return "[" + ", ".join("0x{:02x}".format(byte) for byte in data) + "]"

    def _check_word(self, word: int, name: str = "value"):
        """Checks that a word is a valid two-byte value and throws otherwise.
        Parameters:
            word: integer value to check.
            name (optional): name of the variable to include in the error.
        """
        if not 0 <= word <= 0xFFFF:
            raise ValueError(
                f"{name} outside valid two-byte word range: {word}")

    def _word_or_none(self, response: list):
        """Unpacks an I2C response as either a single 2-byte word or None.
        Parameters:
            response: None or a single-value list.
        Returns:
            None or the single value inside 'response'.
        """
        return next(iter(response or []), None)

    def _crc8(self, word: int):
        """Computes the CRC-8 checksum as per the SCD30 interface description.
        Parameters:
            word: two-byte integer word value to compute the checksum over.
        Returns:
            single-byte integer CRC-8 checksum.
        Polynomial: x^8 + x^5 + x^4 + 1 (0x31, MSB)
        Initialization: 0xFF
        Algorithm adapted from:
        https://en.wikipedia.org/wiki/Computation_of_cyclic_redundancy_checks
        """
        self._check_word(word, "word")
        polynomial = 0x31
        rem = 0xFF
        word_bytes = word.to_bytes(2, "big")
        for byte in word_bytes:
            rem ^= byte
            for _ in range(8):
                if rem & 0x80:
                    rem = (rem << 1) ^ polynomial
                else:
                    rem = rem << 1
                rem &= 0xFF

        return rem

    def _send_command(self, command: int, num_response_words: int = 1,
                      arguments: list = []):
        """Sends the provided I2C command and reads out the results.
        Parameters:
            command: the two-byte command code, e.g. 0x0010.
            num_response_words: number of two-byte words in the result.
            arguments (optional): list of two-byte arguments to the command.
        Returns:
            list of num_response_words two-byte int values from the sensor.
        """
        self._check_word(command, "command")
        logging.debug(f"Executing command {self._pretty_hex(command)} with "
                      f"arguments: {self._pretty_hex(arguments)}")

        raw_message = list(command.to_bytes(2, "big"))
        for argument in arguments:
            self._check_word(argument, "argument")
            raw_message.extend(argument.to_bytes(2, "big"))
            raw_message.append(self._crc8(argument))

        logging.debug(
            f"Sending raw I2C data block: {self._pretty_hex(raw_message)}")

        # self._i2c.write_i2c_block_data(self.address, command, arguments)
        write_txn = i2c_msg.write(self.address, raw_message)
        self.bus.i2c_rdwr(write_txn)

        # The interface description suggests a >3ms delay between writes and
        # reads for most commands.
        time.sleep(timedelta(milliseconds=5).total_seconds())

        if num_response_words == 0:
            return []

        read_txn = i2c_msg.read(self.address, num_response_words * 3)
        self.bus.i2c_rdwr(read_txn)

        # raw_response = self._i2c.read_i2c_block_data(
        #    self.address, command, 3 * num_response_words)
        raw_response = list(read_txn)
        logging.debug("Received raw I2C response: " +
                      self._pretty_hex(raw_response))

        if len(raw_response) != 3 * num_response_words:
            logging.error(f"Wrong response length: {len(raw_response)} "
                          f"(expected {3 * num_response_words})")

        # Data is returned as a sequence of num_response_words 2-byte words
        # (big-endian), each with a CRC-8 checksum:
        # [MSB0, LSB0, CRC0, MSB1, LSB1, CRC1, ...]
        response = []
        for i in range(num_response_words):
            # word_with_crc contains [MSB, LSB, CRC] for the i-th response word
            word_with_crc = raw_response[3 * i: 3 * i + 3]
            word = int.from_bytes(word_with_crc[:2], "big")
            response_crc = word_with_crc[2]
            computed_crc = self._crc8(word)
            if (response_crc != computed_crc):
                logging.error(
                    f"CRC verification for word {self._pretty_hex(word)} "
                    f"failed: received {self._pretty_hex(response_crc)}, "
                    f"computed {self._pretty_hex(computed_crc)}")
                return None
            response.append(word)

        logging.debug(f"CRC-verified response: {self._pretty_hex(response)}")
        return response

    def get_firmware_version(self):
        """Reads the firmware version from the sensor.
        Returns:
            two-byte integer version number
        """
        return self._word_or_none(self._send_command(0xD100))

    def get_data_ready(self):
        return self._word_or_none(self._send_command(0x0202))

    def start_periodic_measurement(self, ambient_pressure: int = 0):
        """Starts periodic measurement of CO2 concentration, humidity and temp.
        Parameters:
            ambient_pressure (optional): external pressure reading in millibars.
        The enable status of periodic measurement is stored in non-volatile
        memory onboard the sensor module and will persist after shutdown.
        ambient_pressure may be set to either 0 to disable ambient pressure
        compensation, or between [700; 1400] mBar.
        """
        if ambient_pressure and not 700 <= ambient_pressure <= 1400:
            raise ValueError("Ambient pressure must be set to either 0 or in "
                             "the range [700; 1400] mBar")

        self._send_command(0x0010, num_response_words=0,
                           arguments=[ambient_pressure])

    def stop_periodic_measurement(self):
        """Stops periodic measurement of CO2 concentration, humidity and temp.
        The enable status of periodic measurement is stored in non-volatile
        memory onboard the sensor module and will persist after shutdown.
        """
        self._send_command(0x0104, num_response_words=0)

    def get_measurement_interval(self):
        """Gets the interval used for periodic measurements.
        Returns:
            measurement interval in seconds or None.
        """
        interval = self._word_or_none(self._send_command(0x4600, 1))

        if interval is None or not 2 <= interval <= 1800:
            logging.error("Failed to read measurement interval, received: " +
                          self._pretty_hex(interval))

        return interval

    def set_measurement_interval(self, interval=2):
        """Sets the interval used for periodic measurements.
        Parameters:
            interval: the interval in seconds within the range [2; 1800].
        The interval setting is stored in non-volatile memory and persists
        after power-off.
        """
        if not 2 <= interval <= 1800:
            raise ValueError("Interval must be in the range [2; 1800] (sec)")

        self._send_command(0x4600, 1, [interval])

    def read_measurement(self):
        """Reads out a CO2, temperature and humidity measurement.
        Must only be called if a measurement is available for reading, i.e.
        get_data_ready() returned 1.
        Returns:
            tuple of measurement values (CO2 ppm, Temp 'C, RH %) or None.
        """
        data = self._send_command(0x0300, num_response_words=6)

        if data is None or len(data) != 6:
            logging.error("Failed to read measurement, received: " +
                          self._pretty_hex(data))
            return None

        co2_ppm = interpret_as_float((data[0] << 16) | data[1])
        temp_celsius = interpret_as_float((data[2] << 16) | data[3])
        rh_percent = interpret_as_float((data[4] << 16) | data[5])

        return (co2_ppm, temp_celsius, rh_percent)

    def set_auto_self_calibration(self, active: bool):
        """(De-)activates the automatic self-calibration feature.
        Parameters:
            active: True to enable, False to disable.
        The setting is persisted in non-volatile memory.
        """
        arg = 1 if active else 0
        self._send_command(0x5306, num_response_words=0, arguments=[arg])

    def get_auto_self_calibration_active(self):
        """Gets the automatic self-calibration feature status.
        Returns:
            1 if ASC is active, 0 if inactive, or None upon error.
        """
        return self._word_or_none(self._send_command(0x5306))

    def get_temperature_offset(self):
        """Gets the currently active temperature offset.
        The temperature offset is used to compensate for reading bias caused by
        heat generated by nearby electrical components or the SCD30 itself.
        See the documentation of set_temperature_offset for more details on
        calculating the offset value correctly.
        The temperature offset is stored in non-volatile memory and persists
        across shutdowns.
        Returns:
            Temperature offset floating-point value in degrees Celsius.
        """
        offset_ticks = self._word_or_none(self._send_command(0x5403))
        if offset_ticks is None:
            return None
        return offset_ticks / 100.0

    def set_temperature_offset(self, offset: float):
        """Sets a new temperature offset.
        The correct temperature offset will vary depending on the installation
        of the sensor as well as its configuration; different measurement
        intervals will result in different power draw, and thus, different
        amounts of electrical heating.
        To compute the offset value for any fixed configuration:
            1. Install and configure the sensor as needed.
            2. Start continuous measurement and let it run for at least 10
               minutes or until a stable temperature equilibrium is reached.
            3. Get the previous temperature offset value T_offset_old from
               the SCD30 using get_temperature_offset.
            4. Get a temperature reading T_measured from the SCD30 using
               read_measurement.
            5. Measure the ambient temperature T_ambient using a *different*
               sensor, away from the immediate proximity of the SCD30.
            6. Compute the new offset to set as follows:
               T_offset_new = (T_measured + T_offset_old) - T_ambient
        After setting a new value, allow the sensor readings to stabilize,
        which will happen slowly and gradually.
        For more details, see the documentation on the project page.
        Arguments:
            offset: temperature offset floating-point value in degrees Celsius.
        """
        offset_ticks = int(offset * 100)
        return self._send_command(0x5403, 0, [offset_ticks])

    def soft_reset(self):
        """Resets the sensor without the need to disconnect power.
        This restarts the onboard system controller and forces the sensor
        back to its power-up state.
        """
        self._send_command(0xD304, num_response_words=0)

if __name__ == '__main__':
    port = 1
    scd30 = SCD30(bus=SMBus(port))
    print("Measures")
    print(scd30.measures())
    i = 0
    while i < 5:
        for m in scd30.measures():
            print(scd30.measure(m))
        
        time.sleep(1)
        i += 1