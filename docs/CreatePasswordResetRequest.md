# CreatePasswordResetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**CreatePasswordResetRequestUser**](CreatePasswordResetRequestUser.md) |  | 

## Example

```python
from winthrop_client_python.models.create_password_reset_request import CreatePasswordResetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePasswordResetRequest from a JSON string
create_password_reset_request_instance = CreatePasswordResetRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePasswordResetRequest.to_json())

# convert the object into a dict
create_password_reset_request_dict = create_password_reset_request_instance.to_dict()
# create an instance of CreatePasswordResetRequest from a dict
create_password_reset_request_from_dict = CreatePasswordResetRequest.from_dict(create_password_reset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


