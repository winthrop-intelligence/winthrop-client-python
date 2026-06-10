# GamePostSearchResultScheduleIntentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**var_date** | **date** |  | [optional] 
**game_types** | **List[str]** | Game-type designations for this availability marker, as plain display-name strings (e.g. \&quot;Home &amp; Home\&quot;). Intentionally not the full GameType object — unlike GamePost.game_types, this field carries only the name_display values, so it is typed as an array of strings rather than $ref GameType. | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_search_result_schedule_intents_inner import GamePostSearchResultScheduleIntentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultScheduleIntentsInner from a JSON string
game_post_search_result_schedule_intents_inner_instance = GamePostSearchResultScheduleIntentsInner.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultScheduleIntentsInner.to_json())

# convert the object into a dict
game_post_search_result_schedule_intents_inner_dict = game_post_search_result_schedule_intents_inner_instance.to_dict()
# create an instance of GamePostSearchResultScheduleIntentsInner from a dict
game_post_search_result_schedule_intents_inner_from_dict = GamePostSearchResultScheduleIntentsInner.from_dict(game_post_search_result_schedule_intents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


