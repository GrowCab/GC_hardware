import click
from time import sleep
from pprint import pprint
import threading
import json
from collections import defaultdict
from HardwareController import VERSION
from HardwareController.BME280 import BME280
from HardwareController.TSL2561 import TSL2561
import GrowCabApi
from GrowCabApi.api.chambers_api import ChambersApi
from GrowCabApi.api.chamber_schedule_api import ChamberScheduleApi
from GrowCabApi.model.configuration import Configuration
from GrowCabApi.model.chamber_status import ChamberStatus
from GrowCabApi.model.error import Error
from GrowCabApi.model.chamber import Chamber as ChamberModel

class_lookup = {
    "BME280": BME280,
    "TSL2561": TSL2561
}

class Chamber:
    def updateSchedule(self):
        print("Updating Schedule")
        thread = threading.Timer(self.update_configuration_frequency, self.updateSchedule)
        thread.daemon = True
        thread.start()
        api_chamber_schedule = ChamberScheduleApi(api_client=self.api_client).get_chamber_schedule(chamber_id=1)
        self.chamber_schedule = api_chamber_schedule
        # TODO: Update actuator states based on the configuration

    def __init__(self, api_client, update_configuration_frequency):

        # This function should raise an exception in case anything goes awry
        self.api_client = api_client
        self.update_configuration_frequency = update_configuration_frequency
        api_chamber = ChambersApi(api_client=api_client).get_chamber(chamber_id=1)
        api_chamber_schedule = ChamberScheduleApi(api_client=api_client).get_chamber_schedule(chamber_id=1)

        self.chamber_settings = api_chamber
        self.chamber_schedule = api_chamber_schedule

        self.sensors = []

        # Using the class names from the DB, initialise and store in 'self.sensors' the hardware
        #  sensor instances
        for chamber_sensor in self.chamber_settings['chamber_sensor']:
            self.sensors.append(class_lookup[chamber_sensor['sensor']['hardware_classname']]())

        self.updateSchedule()
        print("Chamber Setup - Done")

        # self.actuators = hardwareActuators()
        # self.registered_sensors = getChamberSensors(self.id)
        # self.registered_actuators = getChamberActuators(self.id)
    
    


@click.command()
@click.option('--api_host', default='http://localhost', show_default=True)
@click.option('--chamber_id', default=1, show_default=True)
@click.option('--measure_frequency', default=3, show_default=True)
@click.option('--update_configuration_frequency', default=5, show_default=True)
@click.version_option()
def main(api_host, chamber_id, measure_frequency, update_configuration_frequency):
    print(f"GC_hardware - {VERSION}")
    print("Press CTRL-C to terminate")
    running = True
    api_client = GrowCabApi.ApiClient(configuration=GrowCabApi.Configuration(host=api_host))
    try:
        chamber = Chamber(api_client, update_configuration_frequency)
        while running:
            print("Measuring: ")
            chamber_current_measures = ChamberStatus()
            chamber_current_measures['data'] = {}
            for s in chamber.sensors:
                print(f"{s}")
                chamber_current_measures['data'][str(s)] = {}
                for measure_type in s.measures():
                    measurement = s.measure(measure_type).value
                    chamber_current_measures['data'][str(s)][measure_type] = measurement
            # TODO: Prepare a MeasureGroup for reporting back to DB
            print(chamber_current_measures)
            ChambersApi(api_client=api_client).put_chamber_status(chamber_id=1, chamber_status=chamber_current_measures)
            print("")

            sleep(measure_frequency)
    except KeyboardInterrupt:
        print("Terminating...")

if __name__ == "__main__":
    main()