# GamePostSearchResultContactCell

Cell/mobile phone. value/dial are null when not on file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**dial** | **str** |  | [optional] 
**present** | **bool** | Whether a cell number is on file. | 

## Example

```python
from winthrop_client_python.models.game_post_search_result_contact_cell import GamePostSearchResultContactCell

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultContactCell from a JSON string
game_post_search_result_contact_cell_instance = GamePostSearchResultContactCell.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultContactCell.to_json())

# convert the object into a dict
game_post_search_result_contact_cell_dict = game_post_search_result_contact_cell_instance.to_dict()
# create an instance of GamePostSearchResultContactCell from a dict
game_post_search_result_contact_cell_from_dict = GamePostSearchResultContactCell.from_dict(game_post_search_result_contact_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


