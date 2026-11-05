# NewAdminPlayerStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_id** | **int** |  | [optional] 
**players** | [**List[PlayerOption]**](PlayerOption.md) |  | [optional] 
**schools** | [**List[IdName]**](IdName.md) |  | [optional] 
**sports** | [**List[IdName]**](IdName.md) |  | [optional] 
**year_options** | **List[int]** |  | [optional] 
**eligible_options** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.new_admin_player_stat import NewAdminPlayerStat

# TODO update the JSON string below
json = "{}"
# create an instance of NewAdminPlayerStat from a JSON string
new_admin_player_stat_instance = NewAdminPlayerStat.from_json(json)
# print the JSON string representation of the object
print(NewAdminPlayerStat.to_json())

# convert the object into a dict
new_admin_player_stat_dict = new_admin_player_stat_instance.to_dict()
# create an instance of NewAdminPlayerStat from a dict
new_admin_player_stat_from_dict = NewAdminPlayerStat.from_dict(new_admin_player_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


