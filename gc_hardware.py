import click
from time import sleep
from pprint import pprint
from HardwareController import VERSION
from HardwareController.BME280 import BME280
from HardwareController.TSL2561 import TSL2561
import GrowCabApi
from GrowCabApi.api.chambers_api import ChambersApi
from GrowCabApi.model.configuration import Configuration
from GrowCabApi.model.error import Error
from GrowCabApi.model.chamber import Chamber

class Chamber:
    def __init__(self, id):
        self.id = id

        # self.actuators = hardwareActuators()
        self.sensors = [BME280(), TSL2561()]
        # self.registered_sensors = getChamberSensors(self.id)
        # self.registered_actuators = getChamberActuators(self.id)


@click.command()
@click.option('--api_host', default='http://localhost', show_default=True)
@click.option('--chamber_id', default=1, show_default=True)
@click.option('--measure_frequency', default=60, show_default=True)
@click.version_option()
def main(api_host, chamber_id, measure_frequency):
    print(f"GC_hardware - {VERSION}")
    print("Press CTRL-C to terminate")
    running = True
    api_client = GrowCabApi.ApiClient(configuration=GrowCabApi.Configuration(host=api_host))
    api_chamber = ChambersApi(api_client=api_client).get_chamber(chamber_id=1)
    print(api_chamber)
    # api_chamber: ApiChamber = get_chamber.sync(client=api_client)
    # print(api_chamber)
    try:
        chamber = Chamber(chamber_id) # TODO: Collect *chamber_id* configuration
        while running:
            print("Measuring: ")
            for s in chamber.sensors:
                for measure_type in s.measures():
                    measurement = s.measure(measure_type)
                    print(f"{measure_type}: {measurement.value:.2f}")
            print("")
            sleep(measure_frequency) # 10s
    except KeyboardInterrupt:
        print("Terminating...")

if __name__ == "__main__":
    main()