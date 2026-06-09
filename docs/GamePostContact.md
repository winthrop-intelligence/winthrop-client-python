# GamePostContact

Contact person for a game post's school and sport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_name** | **str** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**position** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**phone_dial** | **str** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**mobile_phone_dial** | **str** |  | [optional] 
**scheduling_phone** | **str** | User-controlled scheduling phone (textable); null when unset, in which case clients fall back to phone | [optional] 
**scheduling_phone_dial** | **str** | Dial-ready form of the scheduling phone for tel links | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_contact import GamePostContact

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostContact from a JSON string
game_post_contact_instance = GamePostContact.from_json(json)
# print the JSON string representation of the object
print(GamePostContact.to_json())

# convert the object into a dict
game_post_contact_dict = game_post_contact_instance.to_dict()
# create an instance of GamePostContact from a dict
game_post_contact_from_dict = GamePostContact.from_dict(game_post_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


