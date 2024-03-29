# GrowCabApi.ChambersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chamber**](ChambersApi.md#get_chamber) | **GET** /api/chamber/{chamber_id} | Get the chamber and related objects :param chamber_id: ID of the chamber :return: Returns a Chamber object
[**get_chamber_power_status**](ChambersApi.md#get_chamber_power_status) | **GET** /api/chamber/power/{chamber_id} | 
[**get_chamber_sensors**](ChambersApi.md#get_chamber_sensors) | **GET** /api/chamber_sensors/{chamber_id} | Get the sensors for a chamber :param chamber_id: :return:
[**get_chamber_status**](ChambersApi.md#get_chamber_status) | **GET** /api/chamber_status/{chamber_id} | 
[**get_chamber_units**](ChambersApi.md#get_chamber_units) | **GET** /api/chamber_units/{chamber_id} | Get the units available for this chamber
[**get_chambers**](ChambersApi.md#get_chambers) | **GET** /api/chambers | Get the list of configurations
[**put_chamber_status**](ChambersApi.md#put_chamber_status) | **PUT** /api/chamber_status/{chamber_id} | 
[**set_chamber_power_status**](ChambersApi.md#set_chamber_power_status) | **PUT** /api/chamber/power/{chamber_id} | 


# **get_chamber**
> Chamber get_chamber(chamber_id)

Get the chamber and related objects :param chamber_id: ID of the chamber :return: Returns a Chamber object

### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import chambers_api
from GrowCabApi.model.error import Error
from GrowCabApi.model.chamber import Chamber
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = GrowCabApi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with GrowCabApi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = chambers_api.ChambersApi(api_client)
    chamber_id = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get the chamber and related objects :param chamber_id: ID of the chamber :return: Returns a Chamber object
        api_response = api_instance.get_chamber(chamber_id)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ChambersApi->get_chamber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | **int**|  |

### Return type

[**Chamber**](Chamber.md)

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

# **get_chamber_power_status**
> ChamberPowerStatus get_chamber_power_status(chamber_id)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import chambers_api
from GrowCabApi.model.chamber_power_status import ChamberPowerStatus
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
    api_instance = chambers_api.ChambersApi(api_client)
    chamber_id = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_chamber_power_status(chamber_id)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ChambersApi->get_chamber_power_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | **int**|  |

### Return type

[**ChamberPowerStatus**](ChamberPowerStatus.md)

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

# **get_chamber_sensors**
> [SensorUnit] get_chamber_sensors(chamber_id)

Get the sensors for a chamber :param chamber_id: :return:

### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import chambers_api
from GrowCabApi.model.sensor_unit import SensorUnit
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
    api_instance = chambers_api.ChambersApi(api_client)
    chamber_id = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get the sensors for a chamber :param chamber_id: :return:
        api_response = api_instance.get_chamber_sensors(chamber_id)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ChambersApi->get_chamber_sensors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | **int**|  |

### Return type

[**[SensorUnit]**](SensorUnit.md)

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

# **get_chamber_status**
> MeasureGroup get_chamber_status(chamber_id)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import chambers_api
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
    api_instance = chambers_api.ChambersApi(api_client)
    chamber_id = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_chamber_status(chamber_id)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ChambersApi->get_chamber_status: %s\n" % e)
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

# **get_chamber_units**
> [Unit] get_chamber_units(chamber_id)

Get the units available for this chamber

This is useful for understanding which dials to present but also which values to use for filtering/separating the ExpectedMeasure(s) of a Configuration for a Chamber :param chamber_id: ID of the chamber :return: Returns a list of Unit objects

### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import chambers_api
from GrowCabApi.model.unit import Unit
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
    api_instance = chambers_api.ChambersApi(api_client)
    chamber_id = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get the units available for this chamber
        api_response = api_instance.get_chamber_units(chamber_id)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ChambersApi->get_chamber_units: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | **int**|  |

### Return type

[**[Unit]**](Unit.md)

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

# **get_chambers**
> [Chamber] get_chambers()

Get the list of configurations

### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import chambers_api
from GrowCabApi.model.error import Error
from GrowCabApi.model.chamber import Chamber
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = GrowCabApi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with GrowCabApi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = chambers_api.ChambersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the list of configurations
        api_response = api_instance.get_chambers()
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ChambersApi->get_chambers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Chamber]**](Chamber.md)

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

# **put_chamber_status**
> [Measure] put_chamber_status(chamber_id, chamber_status)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import chambers_api
from GrowCabApi.model.chamber_status import ChamberStatus
from GrowCabApi.model.measure import Measure
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
    api_instance = chambers_api.ChambersApi(api_client)
    chamber_id = 0 # int | 
    chamber_status = ChamberStatus(
        data={
            "key": {},
        },
    ) # ChamberStatus | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_chamber_status(chamber_id, chamber_status)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ChambersApi->put_chamber_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | **int**|  |
 **chamber_status** | [**ChamberStatus**](ChamberStatus.md)|  |

### Return type

[**[Measure]**](Measure.md)

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

# **set_chamber_power_status**
> Chamber set_chamber_power_status(chamber_id, chamber_power_status)



### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import chambers_api
from GrowCabApi.model.chamber_power_status import ChamberPowerStatus
from GrowCabApi.model.error import Error
from GrowCabApi.model.chamber import Chamber
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = GrowCabApi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with GrowCabApi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = chambers_api.ChambersApi(api_client)
    chamber_id = 0 # int | 
    chamber_power_status = ChamberPowerStatus(
        status=None,
    ) # ChamberPowerStatus | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_chamber_power_status(chamber_id, chamber_power_status)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ChambersApi->set_chamber_power_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | **int**|  |
 **chamber_power_status** | [**ChamberPowerStatus**](ChamberPowerStatus.md)|  |

### Return type

[**Chamber**](Chamber.md)

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

