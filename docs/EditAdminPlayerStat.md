# EditAdminPlayerStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_stat** | [**AdminPlayerStat**](AdminPlayerStat.md) |  | [optional] 
**players** | [**List[PlayerOption]**](PlayerOption.md) |  | [optional] 
**schools** | [**List[IdName]**](IdName.md) |  | [optional] 
**sports** | [**List[IdName]**](IdName.md) |  | [optional] 
**year_options** | **List[int]** |  | [optional] 
**eligible_options** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.edit_admin_player_stat import EditAdminPlayerStat

# TODO update the JSON string below
json = "{}"
# create an instance of EditAdminPlayerStat from a JSON string
edit_admin_player_stat_instance = EditAdminPlayerStat.from_json(json)
# print the JSON string representation of the object
print(EditAdminPlayerStat.to_json())

# convert the object into a dict
edit_admin_player_stat_dict = edit_admin_player_stat_instance.to_dict()
# create an instance of EditAdminPlayerStat from a dict
edit_admin_player_stat_from_dict = EditAdminPlayerStat.from_dict(edit_admin_player_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


