# smooch.AppApi

All URIs are relative to *https://api.smooch.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](AppApi.md#create_app) | **POST** /apps | 
[**create_secret_key**](AppApi.md#create_secret_key) | **POST** /apps/{appId}/keys | 
[**delete_app**](AppApi.md#delete_app) | **DELETE** /apps/{appId} | 
[**delete_secret_key**](AppApi.md#delete_secret_key) | **DELETE** /apps/{appId}/keys/{keyId} | 
[**get_app**](AppApi.md#get_app) | **GET** /apps/{appId} | 
[**get_app_jwt**](AppApi.md#get_app_jwt) | **GET** /apps/{appId}/keys/{keyId}/jwt | 
[**get_secret_key**](AppApi.md#get_secret_key) | **GET** /apps/{appId}/keys/{keyId} | 
[**list_apps**](AppApi.md#list_apps) | **GET** /apps | 
[**list_secret_keys**](AppApi.md#list_secret_keys) | **GET** /apps/{appId}/keys | 


# **create_app**
> AppResponse create_app(app_create_body)



Create a new app.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_create_body = smooch.AppCreate() # AppCreate | Body for a createApp request.

try:
    api_response = api_instance.create_app(app_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->create_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_create_body** | [**AppCreate**](AppCreate.md)| Body for a createApp request. | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_secret_key**
> SecretKeyResponse create_secret_key(app_id, secret_key_create_body)



Create a secret key for the specified app.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.
secret_key_create_body = smooch.SecretKeyCreate() # SecretKeyCreate | Body for a createSecretKey request.

try:
    api_response = api_instance.create_secret_key(app_id, secret_key_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->create_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **secret_key_create_body** | [**SecretKeyCreate**](SecretKeyCreate.md)| Body for a createSecretKey request. | 

### Return type

[**SecretKeyResponse**](SecretKeyResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app**
> delete_app(app_id)



Delete the specified app.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.

try:
    api_instance.delete_app(app_id)
except ApiException as e:
    print("Exception when calling AppApi->delete_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret_key**
> delete_secret_key(app_id, key_id)



Delete the specified secret key.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.
key_id = 'key_id_example' # str | Identifies the secret key.

try:
    api_instance.delete_secret_key(app_id, key_id)
except ApiException as e:
    print("Exception when calling AppApi->delete_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **key_id** | **str**| Identifies the secret key. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> AppResponse get_app(app_id)



Get the specified app.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.

try:
    api_response = api_instance.get_app(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_jwt**
> JwtResponse get_app_jwt(app_id, key_id)



Get an app-scoped JWT for the specified secret key.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.
key_id = 'key_id_example' # str | Identifies the secret key.

try:
    api_response = api_instance.get_app_jwt(app_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_app_jwt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **key_id** | **str**| Identifies the secret key. | 

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_key**
> SecretKeyResponse get_secret_key(app_id, key_id)



Get the specified secret key.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.
key_id = 'key_id_example' # str | Identifies the secret key.

try:
    api_response = api_instance.get_secret_key(app_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **key_id** | **str**| Identifies the secret key. | 

### Return type

[**SecretKeyResponse**](SecretKeyResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps**
> ListAppsResponse list_apps(limit=limit, offset=offset)



List all apps configured.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
limit = 56 # int | The number of records to return. (optional)
offset = 56 # int | The number of initial records to skip before picking records to return. (optional)

try:
    api_response = api_instance.list_apps(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->list_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of records to return. | [optional] 
 **offset** | **int**| The number of initial records to skip before picking records to return. | [optional] 

### Return type

[**ListAppsResponse**](ListAppsResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secret_keys**
> ListSecretKeysResponse list_secret_keys(app_id)



List the secret keys for the specified app.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.

try:
    api_response = api_instance.list_secret_keys(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->list_secret_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

[**ListSecretKeysResponse**](ListSecretKeysResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

