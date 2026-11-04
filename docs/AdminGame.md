# AdminGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**home_school_score** | **int** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**away_school_score** | **int** |  | [optional] 
**overtime** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**game_date** | **date** |  | [optional] 
**season_year_tbd** | **int** |  | [optional] 
**game_contract_id** | **int** |  | [optional] 
**city** | **str** |  | [optional] 
**state_id** | **int** |  | [optional] 
**neutral** | **bool** |  | [optional] 
**in_conference** | **bool** |  | [optional] 
**home_school** | [**AdminGameSchoolRef**](AdminGameSchoolRef.md) |  | [optional] 
**away_school** | [**AdminGameSchoolRef**](AdminGameSchoolRef.md) |  | [optional] 
**sport** | [**AdminGameSportRef**](AdminGameSportRef.md) |  | [optional] 
**state** | [**AdminGameStateRef**](AdminGameStateRef.md) |  | [optional] 
**game_contract_display** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_game import AdminGame

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGame from a JSON string
admin_game_instance = AdminGame.from_json(json)
# print the JSON string representation of the object
print(AdminGame.to_json())

# convert the object into a dict
admin_game_dict = admin_game_instance.to_dict()
# create an instance of AdminGame from a dict
admin_game_from_dict = AdminGame.from_dict(admin_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


