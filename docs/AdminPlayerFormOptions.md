# AdminPlayerFormOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schools** | [**List[IdName]**](IdName.md) |  | [optional] 
**sports** | [**List[IdName]**](IdName.md) |  | [optional] 
**eligible_options** | **List[str]** |  | [optional] 
**year_options** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_form_options import AdminPlayerFormOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerFormOptions from a JSON string
admin_player_form_options_instance = AdminPlayerFormOptions.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerFormOptions.to_json())

# convert the object into a dict
admin_player_form_options_dict = admin_player_form_options_instance.to_dict()
# create an instance of AdminPlayerFormOptions from a dict
admin_player_form_options_from_dict = AdminPlayerFormOptions.from_dict(admin_player_form_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


