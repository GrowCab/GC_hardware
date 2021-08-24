from logging import error
from HardwareController.Chamber import Chamber
import click
from time import sleep
from pprint import pp, pprint
from datetime import datetime
from HardwareController import VERSION
import signal
import sys
import GrowCabApi

chamber = None

@click.command()
@click.option('--api_host', default='http://localhost:5000', show_default=True)
@click.option('--chamber_id', default=1, show_default=True)
@click.option('--save_status_frequency', default=30, show_default=True, help="Save the measured status each X seconds")
@click.option('--update_configuration_frequency', default=5, show_default=True)
@click.version_option()
def main(api_host, chamber_id, save_status_frequency, update_configuration_frequency):
    print(f"GC_hardware - {VERSION}")
    print("Press CTRL-C to terminate")
    running = True
    api_client = GrowCabApi.ApiClient(configuration=GrowCabApi.Configuration(host=api_host))
    try:
        chamber = Chamber(api_client, update_configuration_frequency)
        time = 0

        while running:
            #print("updating sensor data...")
            chamber.updateSensorData()
            if time % save_status_frequency == 0:    
                #print("Current status....")
                #print(chamber.current_status)
                chamber.saveSensorData()
            if time % update_configuration_frequency == 0:
                print("Updating schedule....")
                chamber.updateSchedule()
                pprint(chamber.chamber_schedule)
                chamber.currentExpectedMeasures()
                print("Updating actuators....")
                chamber.updateActuators()
                # TODO: Update actuator here, maybe a function that wraps the two operations "updateChamber"
            sleep(1)
            time += 1
            
    except:
        print("Terminating...")
        if chamber != None:
            chamber.stopActuators()
        raise 

def handler(signum, frame):
    print(f"Terminating ({signum}:{signal.strsignal(signum)})...")
    if chamber != None:
        chamber.stopActuators()
    exit(0  )

signal.signal(signal.SIGABRT, handler)
signal.signal(signal.SIGILL, handler)
signal.signal(signal.SIGHUP, handler)
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGQUIT, handler)
signal.signal(signal.SIGTERM, handler)


if __name__ == "__main__":
    main()