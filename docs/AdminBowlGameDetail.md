# AdminBowlGameDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**postseason_results** | [**List[AdminBowlGamePostseasonResult]**](AdminBowlGamePostseasonResult.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_bowl_game_detail import AdminBowlGameDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdminBowlGameDetail from a JSON string
admin_bowl_game_detail_instance = AdminBowlGameDetail.from_json(json)
# print the JSON string representation of the object
print(AdminBowlGameDetail.to_json())

# convert the object into a dict
admin_bowl_game_detail_dict = admin_bowl_game_detail_instance.to_dict()
# create an instance of AdminBowlGameDetail from a dict
admin_bowl_game_detail_from_dict = AdminBowlGameDetail.from_dict(admin_bowl_game_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


