# AdminGamesMassUpdateStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminGamesMassUpdateStatusMeta**](AdminGamesMassUpdateStatusMeta.md) |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_games_mass_update_status import AdminGamesMassUpdateStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGamesMassUpdateStatus from a JSON string
admin_games_mass_update_status_instance = AdminGamesMassUpdateStatus.from_json(json)
# print the JSON string representation of the object
print(AdminGamesMassUpdateStatus.to_json())

# convert the object into a dict
admin_games_mass_update_status_dict = admin_games_mass_update_status_instance.to_dict()
# create an instance of AdminGamesMassUpdateStatus from a dict
admin_games_mass_update_status_from_dict = AdminGamesMassUpdateStatus.from_dict(admin_games_mass_update_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


