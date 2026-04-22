# TeamScheduleSearchResultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TeamScheduleSearchResult]**](TeamScheduleSearchResult.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**school_count** | **int** | Total number of schools for the sport | [optional] 
**season_year** | **int** | Current schedule season year | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_search_result_collection import TeamScheduleSearchResultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleSearchResultCollection from a JSON string
team_schedule_search_result_collection_instance = TeamScheduleSearchResultCollection.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleSearchResultCollection.to_json())

# convert the object into a dict
team_schedule_search_result_collection_dict = team_schedule_search_result_collection_instance.to_dict()
# create an instance of TeamScheduleSearchResultCollection from a dict
team_schedule_search_result_collection_from_dict = TeamScheduleSearchResultCollection.from_dict(team_schedule_search_result_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


