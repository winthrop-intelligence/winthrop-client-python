# AdminBowlGamePostseasonResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**season_id** | **int** |  | [optional] 
**won** | **bool** |  | [optional] 
**season_school** | **str** |  | [optional] 
**season_sport** | **str** |  | [optional] 
**season_year** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_bowl_game_postseason_result import AdminBowlGamePostseasonResult

# TODO update the JSON string below
json = "{}"
# create an instance of AdminBowlGamePostseasonResult from a JSON string
admin_bowl_game_postseason_result_instance = AdminBowlGamePostseasonResult.from_json(json)
# print the JSON string representation of the object
print(AdminBowlGamePostseasonResult.to_json())

# convert the object into a dict
admin_bowl_game_postseason_result_dict = admin_bowl_game_postseason_result_instance.to_dict()
# create an instance of AdminBowlGamePostseasonResult from a dict
admin_bowl_game_postseason_result_from_dict = AdminBowlGamePostseasonResult.from_dict(admin_bowl_game_postseason_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


