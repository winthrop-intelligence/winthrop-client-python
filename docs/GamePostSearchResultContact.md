# GamePostSearchResultContact

WINAD-10053: the school+sport scheduling contact for this card, sourced exactly like the /schedules grid (the first Contact for the school+sport and its coach). Each method (office/cell/email) carries an explicit present flag so the card renders \"not on file\" for a missing method rather than faking a value. Null when the school+sport has no contact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Contact coach&#39;s full name. | 
**title** | **str** | The contact coach&#39;s designation (e.g. \&quot;Associate AD\&quot;); null when none is on file. | [optional] 
**office** | [**GamePostSearchResultContactOffice**](GamePostSearchResultContactOffice.md) |  | 
**cell** | [**GamePostSearchResultContactCell**](GamePostSearchResultContactCell.md) |  | 
**email** | [**GamePostSearchResultContactEmail**](GamePostSearchResultContactEmail.md) |  | 
**scheduling_phone** | **str** | User-controlled scheduling phone override (WINAD-9620); null when unset, in which case the UI falls back to the office number. | [optional] 
**scheduling_phone_dial** | **str** | Dial-ready form of the scheduling phone override. | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_search_result_contact import GamePostSearchResultContact

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultContact from a JSON string
game_post_search_result_contact_instance = GamePostSearchResultContact.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultContact.to_json())

# convert the object into a dict
game_post_search_result_contact_dict = game_post_search_result_contact_instance.to_dict()
# create an instance of GamePostSearchResultContact from a dict
game_post_search_result_contact_from_dict = GamePostSearchResultContact.from_dict(game_post_search_result_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


