# TeamScheduleFavoriteDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**favoritable_id** | **str** |  | [optional] 
**favorites_category_id** | **int** |  | [optional] 
**category_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_favorite_detail import TeamScheduleFavoriteDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleFavoriteDetail from a JSON string
team_schedule_favorite_detail_instance = TeamScheduleFavoriteDetail.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleFavoriteDetail.to_json())

# convert the object into a dict
team_schedule_favorite_detail_dict = team_schedule_favorite_detail_instance.to_dict()
# create an instance of TeamScheduleFavoriteDetail from a dict
team_schedule_favorite_detail_from_dict = TeamScheduleFavoriteDetail.from_dict(team_schedule_favorite_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


