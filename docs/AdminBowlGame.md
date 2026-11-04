# AdminBowlGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_bowl_game import AdminBowlGame

# TODO update the JSON string below
json = "{}"
# create an instance of AdminBowlGame from a JSON string
admin_bowl_game_instance = AdminBowlGame.from_json(json)
# print the JSON string representation of the object
print(AdminBowlGame.to_json())

# convert the object into a dict
admin_bowl_game_dict = admin_bowl_game_instance.to_dict()
# create an instance of AdminBowlGame from a dict
admin_bowl_game_from_dict = AdminBowlGame.from_dict(admin_bowl_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


