# PostseasonResult

The furthest postseason stage a season reached (one row per season). Either the bowl_game_* or the tournament_* fields are set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**season_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**season_year** | **int** |  | [optional] 
**bowl_game_id** | **int** |  | [optional] 
**bowl_game_name** | **str** |  | [optional] 
**tournament_round_id** | **int** |  | [optional] 
**tournament_round_name** | **str** |  | [optional] 
**round** | **int** | Round number within the tournament | [optional] 
**tournament_id** | **int** |  | [optional] 
**tournament_name** | **str** |  | [optional] 
**won** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.postseason_result import PostseasonResult

# TODO update the JSON string below
json = "{}"
# create an instance of PostseasonResult from a JSON string
postseason_result_instance = PostseasonResult.from_json(json)
# print the JSON string representation of the object
print(PostseasonResult.to_json())

# convert the object into a dict
postseason_result_dict = postseason_result_instance.to_dict()
# create an instance of PostseasonResult from a dict
postseason_result_from_dict = PostseasonResult.from_dict(postseason_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


