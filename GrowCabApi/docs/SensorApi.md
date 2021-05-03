# GrowCabApi.SensorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sensor**](SensorApi.md#delete_sensor) | **DELETE** /api/sensor/{sensor_id} | 
[**get_sensor**](SensorApi.md#get_sensor) | **GET** /api/sensor/{sensor_id} | 
[**patch_sensor**](SensorApi.md#patch_sensor) | **PATCH** /api/sensor/{sensor_id} | 


# **delete_sensor**
> Error delete_sensor(sensor_id)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import sensor_api
from GrowCabApi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = GrowCabApi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with GrowCabApi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sensor_api.SensorApi(api_client)
    sensor_id = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_sensor(sensor_id)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling SensorApi->delete_sensor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **int**|  |

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensor**
> Sensor get_sensor(sensor_id)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import sensor_api
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
    api_instance = sensor_api.SensorApi(api_client)
    sensor_id = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sensor(sensor_id)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling SensorApi->get_sensor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **int**|  |

### Return type

[**Sensor**](Sensor.md)

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

# **patch_sensor**
> Sensor patch_sensor(sensor_id, sensor)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import sensor_api
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
    api_instance = sensor_api.SensorApi(api_client)
    sensor_id = 0 # int | 
    sensor = Sensor(
        chamber=Chamber(
            description="description_example",
            timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
            chamber_sensor=[
                ChamberSensor(
                    sensor_id=1,
                    sensor=Sensor(Sensor),
                ),
            ],
            id=1,
        ),
        description="description_example",
        hardware_classname="hardware_classname_example",
        timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Sensor | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_sensor(sensor_id, sensor)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling SensorApi->patch_sensor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **int**|  |
 **sensor** | [**Sensor**](Sensor.md)|  |

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

