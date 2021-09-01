# GrowCabApi.SensorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sensors**](SensorsApi.md#get_sensors) | **GET** /api/sensors | Get the list of sensors
[**put_sensor**](SensorsApi.md#put_sensor) | **PUT** /api/sensors | Stores a new sensor


# **get_sensors**
> [Sensor] get_sensors()

Get the list of sensors

### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import sensors_api
from GrowCabApi.model.error import Error
from GrowCabApi.model.sensor import Sensor
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = GrowCabApi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with GrowCabApi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sensors_api.SensorsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the list of sensors
        api_response = api_instance.get_sensors()
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling SensorsApi->get_sensors: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Sensor]**](Sensor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sensor**
> Sensor put_sensor(editable_sensor)

Stores a new sensor

Each sensor contains an id, description and insertion timestamp

### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import sensors_api
from GrowCabApi.model.error import Error
from GrowCabApi.model.sensor import Sensor
from GrowCabApi.model.editable_sensor import EditableSensor
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = GrowCabApi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with GrowCabApi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sensors_api.SensorsApi(api_client)
    editable_sensor = EditableSensor(
        timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        hardware_classname="hardware_classname_example",
        description="description_example",
        chamber=Chamber(
            chamber_sensor=[
                ChamberSensor(
                    sensor_id=1,
                    sensor=Sensor(
                        timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        hardware_classname="hardware_classname_example",
                        description="description_example",
                        chamber=Chamber(Chamber),
                    ),
                ),
            ],
            id=1,
            description="description_example",
            timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # EditableSensor | 

    # example passing only required values which don't have defaults set
    try:
        # Stores a new sensor
        api_response = api_instance.put_sensor(editable_sensor)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling SensorsApi->put_sensor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **editable_sensor** | [**EditableSensor**](EditableSensor.md)|  |

### Return type

[**Sensor**](Sensor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

