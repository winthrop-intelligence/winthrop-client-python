# AdminPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**external_code** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 
**height** | **int** | Raw editable height in inches | [optional] 
**height_display** | **str** | Formatted height, e.g. \&quot;6&#39;9\&quot; | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player import AdminPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayer from a JSON string
admin_player_instance = AdminPlayer.from_json(json)
# print the JSON string representation of the object
print(AdminPlayer.to_json())

# convert the object into a dict
admin_player_dict = admin_player_instance.to_dict()
# create an instance of AdminPlayer from a dict
admin_player_from_dict = AdminPlayer.from_dict(admin_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


