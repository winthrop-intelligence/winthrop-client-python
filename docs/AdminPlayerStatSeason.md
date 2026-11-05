# AdminPlayerStatSeason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**year_str** | **str** |  | [optional] 
**school** | [**AdminPlayerStatSeasonSchool**](AdminPlayerStatSeasonSchool.md) |  | [optional] 
**sport** | [**IdName**](IdName.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_stat_season import AdminPlayerStatSeason

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerStatSeason from a JSON string
admin_player_stat_season_instance = AdminPlayerStatSeason.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerStatSeason.to_json())

# convert the object into a dict
admin_player_stat_season_dict = admin_player_stat_season_instance.to_dict()
# create an instance of AdminPlayerStatSeason from a dict
admin_player_stat_season_from_dict = AdminPlayerStatSeason.from_dict(admin_player_stat_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


