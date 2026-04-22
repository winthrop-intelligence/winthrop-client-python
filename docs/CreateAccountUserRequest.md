# CreateAccountUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**CreateAccountUserRequestUser**](CreateAccountUserRequestUser.md) |  | 

## Example

```python
from winthrop_client_python.models.create_account_user_request import CreateAccountUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountUserRequest from a JSON string
create_account_user_request_instance = CreateAccountUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAccountUserRequest.to_json())

# convert the object into a dict
create_account_user_request_dict = create_account_user_request_instance.to_dict()
# create an instance of CreateAccountUserRequest from a dict
create_account_user_request_from_dict = CreateAccountUserRequest.from_dict(create_account_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


