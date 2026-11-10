# PostseasonResultInput

Give exactly one of fb_bowl_name and tournament_round_id (bowl_game_id is the deprecated form of fb_bowl_name). The write replaces the season's row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_id** | **int** |  | 
**fb_bowl_name** | **str** | The football bowl as text, no bowl_games row needed. Not blank. Name the game that season without a presenting sponsor (&#39;Pinstripe Bowl&#39;, not &#39;Bad Boy Mowers Pinstripe Bowl&#39;; &#39;Rate Bowl&#39; stays). | [optional] 
**bowl_game_id** | **int** | Deprecated. Its current name is copied into fb_bowl_name. | [optional] 
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


