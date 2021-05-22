from HardwareController.RangeSwitch import RangeSwitch, SwitchEffect
from urllib3.exceptions import MaxRetryError, ResponseError
import sys
from pprint import pp, pprint
from GrowCabApi.api.chambers_api import ChambersApi
from GrowCabApi.api.chamber_schedule_api import ChamberScheduleApi
from GrowCabApi.model.chamber_status import ChamberStatus
from HardwareController.BME280 import BME280
from HardwareController.TSL2561 import TSL2561
from HardwareController.ChamberSchedule import ChamberSchedule
from datetime import datetime

class_lookup = {
    "BME280": BME280,
    "TSL2561": TSL2561
}

class Chamber:
    def updateSchedule(self):
        print("Updating Schedule")
        try:
            api_chamber_schedule = ChamberScheduleApi(api_client=self.api_client).get_chamber_schedule(chamber_id=1)
            self.chamber_schedule = ChamberSchedule(api_chamber_schedule)

        except (ResponseError, MaxRetryError) as e:
            print(f"Encountered an issue when getting the chamber configuration", file=sys.stderr)
            print(f"{e}", file=sys.stderr)

    def __init__(self, api_client, update_configuration_frequency):

        # This function should raise an exception in case anything goes awry
        self.api_client = api_client
        self.chamber_settings = None
        self.chamber_schedule = None
        self.update_configuration_frequency = update_configuration_frequency
        print("Chamber Setup - Started")
        try:
            api_chamber = ChambersApi(api_client=api_client).get_chamber(chamber_id=1)
            self.chamber_settings = api_chamber
            self.updateSchedule()

        except (ResponseError, MaxRetryError) as e:
            print(f"Encountered an issue when getting the chamber configuration", file=sys.stderr)
            print(f"{e}", file=sys.stderr)

        self.sensors = []

        # Using the class names from the DB, initialise and store in 'self.sensors' the hardware
        #  sensor instances
        if self.chamber_settings:
            for chamber_sensor in self.chamber_settings['chamber_sensor']:
                self.sensors.append(class_lookup[chamber_sensor['sensor']['hardware_classname']]())
        
        # In case the configuration was not loaded from the DB
        if not self.sensors:
            self.sensors.extend([BME280(), TSL2561()])
        self.current_status = self.collectSensorData()
        self.updateSchedule()
        print("Chamber Setup - Done")

        #TODO: Make this dynamic
        self.actuators = [
            RangeSwitch(range= 0.5, effect=SwitchEffect.ONOFF, hardware_label="visible_light", control_pin=24 )
            ]
        # self.registered_sensors = getChamberSensors(self.id)
        # self.registered_actuators = getChamberActuators(self.id)

    def collectSensorData(self):
        print("Measuring sensor data")
        chamber_current_measures = ChamberStatus() #The type must be ChamberStatus to be compatible with the backend API. 
        chamber_current_measures['data'] = {}
        for s in self.sensors:
            chamber_current_measures['data'][str(s)] = {}
            for measure_type in s.measures():
                measurement = s.measure(measure_type).value
                chamber_current_measures['data'][str(s)][measure_type] = measurement
        return chamber_current_measures

    def saveSensorData(self):
        try:
            print(f"Saving data to DB")
            ChambersApi(api_client=self.api_client).put_chamber_status(chamber_id=1, chamber_status=self.current_status)
            print (f"Data saved to DB")
        except (ResponseError, MaxRetryError) as e:
            print(f"Could not store the Chamber status in the DB", file=sys.stderr)
            print(f"{e}", file=sys.stderr)

    def updateSensorData(self):
        self.current_status = self.collectSensorData()

    def sensorData(self, hardware_label):
        values = self.current_status['data']
        pprint("Sensor data")
        for sensor in values:
            pprint(f"Sensor: {sensor}")
            for measure_type in values[sensor]:
                pprint(measure_type)
                if measure_type ==  hardware_label:
                    pprint(f"SAAAME {values[sensor][measure_type]}")
                    return values[sensor][measure_type]
        return None

    def updateActuators(self):
        for a in self.actuators:
            pprint("ACTUAAATOR")
            pprint(a)
            if a.effect == SwitchEffect.ONOFF:
                value = self.current_expected_measures[a.hardware_label]['expected_value']
            else:
                value = self.sensorData(a.hardware_label)
            pprint(f"New value {value}")
            a.expected_status = value

    def currentExpectedMeassures(self):
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        print(f'{hour}:{minute}')
        hardware_labels = self.chamber_schedule.hardware_labels()
        pprint(hardware_labels)
        self.current_expected_measures = {}
        for label in hardware_labels:
            expected = self.chamber_schedule.expected_measure_for(unit= label, hour=hour, minute=minute)
            # print(f"------------------{label}------------------------")
            # pprint(self.chamber_schedule.expected_measures_for(label))
            print(f"****************{label}****************")
            pprint(expected)
            self.current_expected_measures[label] = expected
        return self.current_expected_measures