# GC_hardware

## Version management

The version is placed in both the [`setup.py`](../setup.py) file and in the [`HardwareController/__init__.py`](../HardwareController/__init__.py), both of these files can be automatically updated using [bump2version](https://pypi.org/project/bump2version/)


## Installation

The runtime requirements are located in the [requirements.txt](../requirements.txt) file and can be installed using:

```bash
pip install -r requirements.txt
```

This is typically recommended to be done inside a [virtual environment](https://pypi.org/project/virtualenv/), followed by:

```bash
pip install GC_hardware
```

where GC_hardware is the full or relative path to the project folder.


Finally, to execute the daemon:

```bash
python -m HardwareController
```