# TeamScheduleFavoriteEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The favorite record ID | [optional] 
**favoritable_id** | **str** | The FilTeam ID (as string) | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_favorite_entry import TeamScheduleFavoriteEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleFavoriteEntry from a JSON string
team_schedule_favorite_entry_instance = TeamScheduleFavoriteEntry.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleFavoriteEntry.to_json())

# convert the object into a dict
team_schedule_favorite_entry_dict = team_schedule_favorite_entry_instance.to_dict()
# create an instance of TeamScheduleFavoriteEntry from a dict
team_schedule_favorite_entry_from_dict = TeamScheduleFavoriteEntry.from_dict(team_schedule_favorite_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


