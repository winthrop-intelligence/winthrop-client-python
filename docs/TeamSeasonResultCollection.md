# TeamSeasonResultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TeamSeasonResult]**](TeamSeasonResult.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_season_result_collection import TeamSeasonResultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonResultCollection from a JSON string
team_season_result_collection_instance = TeamSeasonResultCollection.from_json(json)
# print the JSON string representation of the object
print(TeamSeasonResultCollection.to_json())

# convert the object into a dict
team_season_result_collection_dict = team_season_result_collection_instance.to_dict()
# create an instance of TeamSeasonResultCollection from a dict
team_season_result_collection_from_dict = TeamSeasonResultCollection.from_dict(team_season_result_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


