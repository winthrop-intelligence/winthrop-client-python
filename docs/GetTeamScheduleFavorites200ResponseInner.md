# GetTeamScheduleFavorites200ResponseInner


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
from winthrop_client_python.models.get_team_schedule_favorites200_response_inner import GetTeamScheduleFavorites200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTeamScheduleFavorites200ResponseInner from a JSON string
get_team_schedule_favorites200_response_inner_instance = GetTeamScheduleFavorites200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetTeamScheduleFavorites200ResponseInner.to_json())

# convert the object into a dict
get_team_schedule_favorites200_response_inner_dict = get_team_schedule_favorites200_response_inner_instance.to_dict()
# create an instance of GetTeamScheduleFavorites200ResponseInner from a dict
get_team_schedule_favorites200_response_inner_from_dict = GetTeamScheduleFavorites200ResponseInner.from_dict(get_team_schedule_favorites200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


