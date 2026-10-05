# DeskSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_version** | **int** | Version returned by GET; submit unchanged when saving. | 
**notifications_enabled** | **bool** |  | [default to False]
**needs_info_emails_enabled** | **bool** | Independently allows Needs info emails. Checked before pausing an ask; a follow-up that was already accepted is still sent if the setting is turned off afterwards. | [default to False]
**copy_email** | **str** | Separate summary recipient. Required and valid when notifications are enabled. | 

## Example

```python
from winthrop_client_python.models.desk_settings import DeskSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DeskSettings from a JSON string
desk_settings_instance = DeskSettings.from_json(json)
# print the JSON string representation of the object
print(DeskSettings.to_json())

# convert the object into a dict
desk_settings_dict = desk_settings_instance.to_dict()
# create an instance of DeskSettings from a dict
desk_settings_from_dict = DeskSettings.from_dict(desk_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


