# PostseasonResultInput

Give exactly one of bowl_game_id and tournament_round_id. The write replaces the season's row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_id** | **int** |  | 
**bowl_game_id** | **int** |  | [optional] 
**tournament_round_id** | **int** | Its tournament must belong to the season&#39;s sport (422 otherwise) | [optional] 
**won** | **bool** |  | 
**change_note** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.postseason_result_input import PostseasonResultInput

# TODO update the JSON string below
json = "{}"
# create an instance of PostseasonResultInput from a JSON string
postseason_result_input_instance = PostseasonResultInput.from_json(json)
# print the JSON string representation of the object
print(PostseasonResultInput.to_json())

# convert the object into a dict
postseason_result_input_dict = postseason_result_input_instance.to_dict()
# create an instance of PostseasonResultInput from a dict
postseason_result_input_from_dict = PostseasonResultInput.from_dict(postseason_result_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


