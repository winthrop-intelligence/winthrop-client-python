# AdminFoiaRequestGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**home_school** | **str** |  | [optional] 
**away_school** | **str** |  | [optional] 
**sport** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**game_date** | **date** |  | [optional] 
**season_year_tbd** | **int** |  | [optional] 
**game_contract** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**neutral** | **bool** |  | [optional] 
**attached** | **bool** |  | [optional] 
**requested_item_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_game import AdminFoiaRequestGame

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestGame from a JSON string
admin_foia_request_game_instance = AdminFoiaRequestGame.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestGame.to_json())

# convert the object into a dict
admin_foia_request_game_dict = admin_foia_request_game_instance.to_dict()
# create an instance of AdminFoiaRequestGame from a dict
admin_foia_request_game_from_dict = AdminFoiaRequestGame.from_dict(admin_foia_request_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


