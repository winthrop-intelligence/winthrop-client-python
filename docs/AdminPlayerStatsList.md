# AdminPlayerStatsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminPlayerStat]**](AdminPlayerStat.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_stats_list import AdminPlayerStatsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerStatsList from a JSON string
admin_player_stats_list_instance = AdminPlayerStatsList.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerStatsList.to_json())

# convert the object into a dict
admin_player_stats_list_dict = admin_player_stats_list_instance.to_dict()
# create an instance of AdminPlayerStatsList from a dict
admin_player_stats_list_from_dict = AdminPlayerStatsList.from_dict(admin_player_stats_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


