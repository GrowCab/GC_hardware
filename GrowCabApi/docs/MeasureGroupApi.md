# GrowCabApi.MeasureGroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_measure_group**](MeasureGroupApi.md#get_latest_measure_group) | **GET** /api/measure_group/{chamber_id} | 
[**put_latest_measure_group**](MeasureGroupApi.md#put_latest_measure_group) | **PUT** /api/measure_group | 


# **get_latest_measure_group**
> MeasureGroup get_latest_measure_group(chamber_id)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import measure_group_api
from GrowCabApi.model.measure_group import MeasureGroup
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
    api_instance = measure_group_api.MeasureGroupApi(api_client)
    chamber_id = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_latest_measure_group(chamber_id)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling MeasureGroupApi->get_latest_measure_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | **int**|  |

### Return type

[**MeasureGroup**](MeasureGroup.md)

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

# **put_latest_measure_group**
> MeasureGroup put_latest_measure_group(editable_measure_group)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import measure_group_api
from GrowCabApi.model.measure_group import MeasureGroup
from GrowCabApi.model.error import Error
from GrowCabApi.model.editable_measure_group import EditableMeasureGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = GrowCabApi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with GrowCabApi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = measure_group_api.MeasureGroupApi(api_client)
    editable_measure_group = EditableMeasureGroup(
        sensor_measure=[
            EditableSensorMeasure(
                sensor_unit_id=1,
                current_value=3.14,
                chamber_sensor_id=1,
            ),
        ],
        actuator_measure=[
            EditableActuatorMeasure(
                current_value=1,
                chamber_actuator_id=1,
            ),
        ],
    ) # EditableMeasureGroup | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_latest_measure_group(editable_measure_group)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling MeasureGroupApi->put_latest_measure_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **editable_measure_group** | [**EditableMeasureGroup**](EditableMeasureGroup.md)|  |

### Return type

[**MeasureGroup**](MeasureGroup.md)

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

