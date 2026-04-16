# GetAccountUserActivation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.get_account_user_activation200_response import GetAccountUserActivation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountUserActivation200Response from a JSON string
get_account_user_activation200_response_instance = GetAccountUserActivation200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccountUserActivation200Response.to_json())

# convert the object into a dict
get_account_user_activation200_response_dict = get_account_user_activation200_response_instance.to_dict()
# create an instance of GetAccountUserActivation200Response from a dict
get_account_user_activation200_response_from_dict = GetAccountUserActivation200Response.from_dict(get_account_user_activation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


