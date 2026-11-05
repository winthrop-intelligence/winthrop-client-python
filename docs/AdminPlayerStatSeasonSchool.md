# AdminPlayerStatSeasonSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**short_name_or_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_stat_season_school import AdminPlayerStatSeasonSchool

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerStatSeasonSchool from a JSON string
admin_player_stat_season_school_instance = AdminPlayerStatSeasonSchool.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerStatSeasonSchool.to_json())

# convert the object into a dict
admin_player_stat_season_school_dict = admin_player_stat_season_school_instance.to_dict()
# create an instance of AdminPlayerStatSeasonSchool from a dict
admin_player_stat_season_school_from_dict = AdminPlayerStatSeasonSchool.from_dict(admin_player_stat_season_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


