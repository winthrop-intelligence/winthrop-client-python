# UpdatePasswordResetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UpdatePasswordResetRequestUser**](UpdatePasswordResetRequestUser.md) |  | 

## Example

```python
from winthrop_client_python.models.update_password_reset_request import UpdatePasswordResetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordResetRequest from a JSON string
update_password_reset_request_instance = UpdatePasswordResetRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePasswordResetRequest.to_json())

# convert the object into a dict
update_password_reset_request_dict = update_password_reset_request_instance.to_dict()
# create an instance of UpdatePasswordResetRequest from a dict
update_password_reset_request_from_dict = UpdatePasswordResetRequest.from_dict(update_password_reset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


