# AdminGameStateRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_game_state_ref import AdminGameStateRef

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGameStateRef from a JSON string
admin_game_state_ref_instance = AdminGameStateRef.from_json(json)
# print the JSON string representation of the object
print(AdminGameStateRef.to_json())

# convert the object into a dict
admin_game_state_ref_dict = admin_game_state_ref_instance.to_dict()
# create an instance of AdminGameStateRef from a dict
admin_game_state_ref_from_dict = AdminGameStateRef.from_dict(admin_game_state_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


