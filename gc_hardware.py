from HardwareController.Chamber import Chamber
import click
from time import sleep
from pprint import pp, pprint
from datetime import datetime
from HardwareController import VERSION
import GrowCabApi



            
    


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
            print("udating sensor data...")
            chamber.updateSensorData()
            if time % save_status_frequency == 0:    
                print("Current status....")
                pprint(chamber.current_status)
                chamber.saveSensorData()
            if time % update_configuration_frequency == 0:
                pprint("Updatign schedule....")
                chamber.updateSchedule()
                pprint(chamber.chamber_schedule)
                chamber.currentExpectedMeassures()
                #
                print("Updating actuators....")
                chamber.updateActuators()
                #TODO: Update actuator here, maybe a functin that wraps the two operations "updateChamber"
            sleep(5)
            time += 1
    except KeyboardInterrupt:
        print("Terminating...")




if __name__ == "__main__":
    main()