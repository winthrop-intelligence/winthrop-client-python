# GameWriteFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_school_id** | **int** |  | [optional] 
**home_school_score** | **int** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**away_school_score** | **int** |  | [optional] 
**overtime** | **int** |  | [optional] 
**sport_id** | **int** |  | 
**description** | **str** |  | [optional] 
**game_date** | **date** |  | [optional] 
**season_year_tbd** | **int** |  | [optional] 
**game_contract_id** | **int** |  | [optional] 
**city** | **str** |  | [optional] 
**state_id** | **int** |  | [optional] 
**neutral** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_write_fields import GameWriteFields

# TODO update the JSON string below
json = "{}"
# create an instance of GameWriteFields from a JSON string
game_write_fields_instance = GameWriteFields.from_json(json)
# print the JSON string representation of the object
print(GameWriteFields.to_json())

# convert the object into a dict
game_write_fields_dict = game_write_fields_instance.to_dict()
# create an instance of GameWriteFields from a dict
game_write_fields_from_dict = GameWriteFields.from_dict(game_write_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


