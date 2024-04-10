# SystemSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**current_season_year** | **int** |  | [optional] 
**current_financials_season_year** | **int** |  | [optional] 
**schedule_season_year** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.system_setting import SystemSetting

# TODO update the JSON string below
json = "{}"
# create an instance of SystemSetting from a JSON string
system_setting_instance = SystemSetting.from_json(json)
# print the JSON string representation of the object
print(SystemSetting.to_json())

# convert the object into a dict
system_setting_dict = system_setting_instance.to_dict()
# create an instance of SystemSetting from a dict
system_setting_form_dict = system_setting.from_dict(system_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


