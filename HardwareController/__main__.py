import click
from time import sleep
from . import VERSION
from .BME280 import BME280
from .TSL2561 import TSL2561

class Chamber:
    def __init__(self, id):
        self.id = id

        # self.actuators = hardwareActuators()
        self.sensors = [BME280(), TSL2561()]
        # self.registered_sensors = getChamberSensors(self.id)
        # self.registered_actuators = getChamberActuators(self.id)


@click.command()
@click.option('--api_endpoint', default='http://localhost:5000/api', show_default=True)
@click.option('--chamber_id', default=1, show_default=True)
@click.option('--measure_frequency', default=60, show_default=True)
@click.version_option()
def main(api_endpoint, chamber_id, measure_frequency):
    print(f"GC_hardware - {VERSION}")
    print("Press CTRL-C to terminate")
    running = True
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