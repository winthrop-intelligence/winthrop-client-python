# GamePostSearchResultContactOffice

Office phone. value/dial are null when not on file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Formatted for display, e.g. \&quot;(509) 555-0196\&quot;. | 
**dial** | **str** | Dial-ready form for tel: links; null when absent. | [optional] 
**present** | **bool** | Whether an office number is on file. | 

## Example

```python
from winthrop_client_python.models.game_post_search_result_contact_office import GamePostSearchResultContactOffice

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultContactOffice from a JSON string
game_post_search_result_contact_office_instance = GamePostSearchResultContactOffice.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultContactOffice.to_json())

# convert the object into a dict
game_post_search_result_contact_office_dict = game_post_search_result_contact_office_instance.to_dict()
# create an instance of GamePostSearchResultContactOffice from a dict
game_post_search_result_contact_office_from_dict = GamePostSearchResultContactOffice.from_dict(game_post_search_result_contact_office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


