import click
import HardwareController

@click.command()
@click.option('--api_endpoint', default='http://localhost:5000/api')
def main(api_endpoint):
    print(f"GC_hardware - {HardwareController.VERSION}")

if __name__ == "__main__":
    main()