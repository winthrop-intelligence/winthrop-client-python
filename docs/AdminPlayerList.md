# AdminPlayerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminPlayer]**](AdminPlayer.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_list import AdminPlayerList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerList from a JSON string
admin_player_list_instance = AdminPlayerList.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerList.to_json())

# convert the object into a dict
admin_player_list_dict = admin_player_list_instance.to_dict()
# create an instance of AdminPlayerList from a dict
admin_player_list_from_dict = AdminPlayerList.from_dict(admin_player_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


