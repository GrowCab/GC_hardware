# GC_hardware

## Version management

The version is placed in both the [`setup.py`](../setup.py) file and in the [`HardwareController/__init__.py`](../HardwareController/__init__.py), both of these files can be automatically updated using [bump2version](https://pypi.org/project/bump2version/)

Now for example, to update the version's patch number you can:

```bash
bump2version patch
```

This will modify both files increasing the patch version number by one, for more information, please read the bump2version docs.


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



## Running the app

Once you have installed it, you can simply run the app by using, the `api_host` parameter defaults to `http://localhost` so will likely need to be adjusted:

```bash
gc_hardware --api_host http://<gc_database_host>:<gc_database_port>
```


For a list of all available parameters and their default values, you can use:

```bash
gc_hardware --help
```

## Generate/Update the API using the OpenAPI spec

Run the following command on the main project directory (GC_hardware), to generate a python package mapping the OpenAPI spec to a python library.

```bash
java -Dcolor -jar openapi-generator-cli.jar generate -i http://gc_database:5000/doc/openapi.json -g python --additional-properties=generateSourceCodeOnly=true --package-name GrowCabApi
```

The command requires the `openapi-generator-cli.jar` which can be downloaded using:

```bash
wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/5.1.0/openapi-generator-cli-5.1.0.jar -O openapi-generator-cli.jar
```
