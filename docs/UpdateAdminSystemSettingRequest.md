# UpdateAdminSystemSettingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_setting** | [**UpdateAdminSystemSettingRequestSystemSetting**](UpdateAdminSystemSettingRequestSystemSetting.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_system_setting_request import UpdateAdminSystemSettingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminSystemSettingRequest from a JSON string
update_admin_system_setting_request_instance = UpdateAdminSystemSettingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminSystemSettingRequest.to_json())

# convert the object into a dict
update_admin_system_setting_request_dict = update_admin_system_setting_request_instance.to_dict()
# create an instance of UpdateAdminSystemSettingRequest from a dict
update_admin_system_setting_request_from_dict = UpdateAdminSystemSettingRequest.from_dict(update_admin_system_setting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


