"""
    GrowCab API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from GrowCabApi.api_client import ApiClient, Endpoint as _Endpoint
from GrowCabApi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from GrowCabApi.model.error import Error
from GrowCabApi.model.sensor import Sensor


class SensorApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __delete_sensor(
            self,
            sensor_id,
            **kwargs
        ):
            """delete_sensor  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_sensor(sensor_id, async_req=True)
            >>> result = thread.get()

            Args:
                sensor_id (int):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Error
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['sensor_id'] = \
                sensor_id
            return self.call_with_http_info(**kwargs)

        self.delete_sensor = _Endpoint(
            settings={
                'response_type': (Error,),
                'auth': [],
                'endpoint_path': '/api/sensor/{sensor_id}',
                'operation_id': 'delete_sensor',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'sensor_id',
                ],
                'required': [
                    'sensor_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'sensor_id',
                ]
            },
            root_map={
                'validations': {
                    ('sensor_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'sensor_id':
                        (int,),
                },
                'attribute_map': {
                    'sensor_id': 'sensor_id',
                },
                'location_map': {
                    'sensor_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_sensor
        )

        def __get_sensor(
            self,
            sensor_id,
            **kwargs
        ):
            """get_sensor  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_sensor(sensor_id, async_req=True)
            >>> result = thread.get()

            Args:
                sensor_id (int):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Sensor
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['sensor_id'] = \
                sensor_id
            return self.call_with_http_info(**kwargs)

        self.get_sensor = _Endpoint(
            settings={
                'response_type': (Sensor,),
                'auth': [],
                'endpoint_path': '/api/sensor/{sensor_id}',
                'operation_id': 'get_sensor',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'sensor_id',
                ],
                'required': [
                    'sensor_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'sensor_id',
                ]
            },
            root_map={
                'validations': {
                    ('sensor_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'sensor_id':
                        (int,),
                },
                'attribute_map': {
                    'sensor_id': 'sensor_id',
                },
                'location_map': {
                    'sensor_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_sensor
        )

        def __patch_sensor(
            self,
            sensor_id,
            sensor,
            **kwargs
        ):
            """patch_sensor  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.patch_sensor(sensor_id, sensor, async_req=True)
            >>> result = thread.get()

            Args:
                sensor_id (int):
                sensor (Sensor):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Sensor
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['sensor_id'] = \
                sensor_id
            kwargs['sensor'] = \
                sensor
            return self.call_with_http_info(**kwargs)

        self.patch_sensor = _Endpoint(
            settings={
                'response_type': (Sensor,),
                'auth': [],
                'endpoint_path': '/api/sensor/{sensor_id}',
                'operation_id': 'patch_sensor',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'sensor_id',
                    'sensor',
                ],
                'required': [
                    'sensor_id',
                    'sensor',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'sensor_id',
                ]
            },
            root_map={
                'validations': {
                    ('sensor_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'sensor_id':
                        (int,),
                    'sensor':
                        (Sensor,),
                },
                'attribute_map': {
                    'sensor_id': 'sensor_id',
                },
                'location_map': {
                    'sensor_id': 'path',
                    'sensor': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__patch_sensor
        )
