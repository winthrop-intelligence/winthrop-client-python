# AdminPlayerStatPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**external_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_stat_player import AdminPlayerStatPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerStatPlayer from a JSON string
admin_player_stat_player_instance = AdminPlayerStatPlayer.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerStatPlayer.to_json())

# convert the object into a dict
admin_player_stat_player_dict = admin_player_stat_player_instance.to_dict()
# create an instance of AdminPlayerStatPlayer from a dict
admin_player_stat_player_from_dict = AdminPlayerStatPlayer.from_dict(admin_player_stat_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


