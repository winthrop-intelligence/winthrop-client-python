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


