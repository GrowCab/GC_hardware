# GrowCabApi.ChamberScheduleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chamber_schedule**](ChamberScheduleApi.md#get_chamber_schedule) | **GET** /api/chamber_schedule/{chamber_id} | 
[**get_chamber_schedule_unit**](ChamberScheduleApi.md#get_chamber_schedule_unit) | **GET** /api/chamber_schedule_unit/{chamber_id}/{unit_id} | 


# **get_chamber_schedule**
> Configuration get_chamber_schedule(chamber_id)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import chamber_schedule_api
from GrowCabApi.model.error import Error
from GrowCabApi.model.configuration import Configuration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = GrowCabApi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with GrowCabApi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = chamber_schedule_api.ChamberScheduleApi(api_client)
    chamber_id = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_chamber_schedule(chamber_id)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ChamberScheduleApi->get_chamber_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | **int**|  |

### Return type

[**Configuration**](Configuration.md)

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

# **get_chamber_schedule_unit**
> [ExpectedMeasure] get_chamber_schedule_unit(chamber_id, unit_id)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import chamber_schedule_api
from GrowCabApi.model.expected_measure import ExpectedMeasure
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
    api_instance = chamber_schedule_api.ChamberScheduleApi(api_client)
    chamber_id = 0 # int | 
    unit_id = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_chamber_schedule_unit(chamber_id, unit_id)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ChamberScheduleApi->get_chamber_schedule_unit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | **int**|  |
 **unit_id** | **int**|  |

### Return type

[**[ExpectedMeasure]**](ExpectedMeasure.md)

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

