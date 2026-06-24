# GamePostSearchResultContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_name** | **str** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**position** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**phone_dial** | **str** |  | [optional] 
**scheduling_phone** | **str** |  | [optional] 
**scheduling_phone_dial** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_search_result_contacts_inner import GamePostSearchResultContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultContactsInner from a JSON string
game_post_search_result_contacts_inner_instance = GamePostSearchResultContactsInner.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultContactsInner.to_json())

# convert the object into a dict
game_post_search_result_contacts_inner_dict = game_post_search_result_contacts_inner_instance.to_dict()
# create an instance of GamePostSearchResultContactsInner from a dict
game_post_search_result_contacts_inner_from_dict = GamePostSearchResultContactsInner.from_dict(game_post_search_result_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


