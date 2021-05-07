# GrowCabApi.ConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configurations**](ConfigurationsApi.md#get_configurations) | **GET** /api/configurations | Get the list of configurations
[**put_configuration**](ConfigurationsApi.md#put_configuration) | **PUT** /api/configurations | Stores a new configuration


# **get_configurations**
> [Configuration] get_configurations()

Get the list of configurations

### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import configurations_api
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
    api_instance = configurations_api.ConfigurationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the list of configurations
        api_response = api_instance.get_configurations()
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ConfigurationsApi->get_configurations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Configuration]**](Configuration.md)

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

# **put_configuration**
> Configuration put_configuration(editable_configuration)

Stores a new configuration

### Example

```python
import time
import GrowCabApi
from GrowCabApi.api import configurations_api
from GrowCabApi.model.editable_configuration import EditableConfiguration
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    editable_configuration = EditableConfiguration(
        description="description_example",
        chamber_id=1,
        expected_measure=[
            ExpectedMeasure(
                end_hour=1,
                unit=Unit(
                    hardware_label="hardware_label_example",
                    description="description_example",
                    label="label_example",
                    id=1,
                ),
                expected_value=3.14,
                unit_id=1,
                end_minute=1,
                id=1,
            ),
        ],
    ) # EditableConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        # Stores a new configuration
        api_response = api_instance.put_configuration(editable_configuration)
        pprint(api_response)
    except GrowCabApi.ApiException as e:
        print("Exception when calling ConfigurationsApi->put_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **editable_configuration** | [**EditableConfiguration**](EditableConfiguration.md)|  |

### Return type

[**Configuration**](Configuration.md)

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

