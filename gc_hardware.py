import click
from time import sleep
from pprint import pprint
import sys
from urllib3.exceptions import MaxRetryError, ResponseError
from HardwareController import VERSION
from HardwareController.BME280 import BME280
from HardwareController.TSL2561 import TSL2561
import GrowCabApi
from GrowCabApi.api.chambers_api import ChambersApi
from GrowCabApi.api.chamber_schedule_api import ChamberScheduleApi
from GrowCabApi.model.chamber_status import ChamberStatus

class_lookup = {
    "BME280": BME280,
    "TSL2561": TSL2561
}

class Chamber:
    def updateSchedule(self):
        print("Updating Schedule")
        try:
            api_chamber_schedule = ChamberScheduleApi(api_client=self.api_client).get_chamber_schedule(chamber_id=1)
            self.chamber_schedule = api_chamber_schedule
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
            api_chamber_schedule = ChamberScheduleApi(api_client=api_client).get_chamber_schedule(chamber_id=1)
            self.chamber_settings = api_chamber
            self.chamber_schedule = api_chamber_schedule
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
        time = 0
        while running:
            if time % measure_frequency == 0:
                collectSensorData(chamber, api_client)
            if time % update_configuration_frequency == 0:
                chamber.updateSchedule()
            sleep(1)
            time += 1
    except KeyboardInterrupt:
        print("Terminating...")

def collectSensorData(chamber, api_client):
    print("Measuring sensor data")
    chamber_current_measures = ChamberStatus()
    chamber_current_measures['data'] = {}
    for s in chamber.sensors:
        chamber_current_measures['data'][str(s)] = {}
        for measure_type in s.measures():
            measurement = s.measure(measure_type).value
            chamber_current_measures['data'][str(s)][measure_type] = measurement
    # TODO: Prepare a MeasureGroup for reporting back to DB
    pprint(chamber_current_measures['data'])
    try:
        print(f"Saving data to DB")
        ChambersApi(api_client=api_client).put_chamber_status(chamber_id=1, chamber_status=chamber_current_measures)
        print (f"Data saved to DB")
    except (ResponseError, MaxRetryError) as e:
        print(f"Could not store the Chamber status in the DB", file=sys.stderr)
        print(f"{e}", file=sys.stderr)


if __name__ == "__main__":
    main()