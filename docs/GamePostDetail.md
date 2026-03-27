# GamePostDetail

Full game post detail with contacts and creator info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**sport_slug** | **str** | Sport name for URL construction (e.g. FOOTBALL, BASKETBALL_M) | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**expires_on** | **date** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**game_types_display** | **str** |  | [optional] 
**can_manage** | **bool** |  | [optional] 
**created_by** | [**GamePostDetailCreatedBy**](GamePostDetailCreatedBy.md) |  | [optional] 
**game_types** | [**List[GameType]**](GameType.md) |  | [optional] 
**contacts** | [**List[GamePostContact]**](GamePostContact.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_detail import GamePostDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostDetail from a JSON string
game_post_detail_instance = GamePostDetail.from_json(json)
# print the JSON string representation of the object
print(GamePostDetail.to_json())

# convert the object into a dict
game_post_detail_dict = game_post_detail_instance.to_dict()
# create an instance of GamePostDetail from a dict
game_post_detail_from_dict = GamePostDetail.from_dict(game_post_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


