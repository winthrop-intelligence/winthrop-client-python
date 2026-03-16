# CreateTeamScheduleFavoriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favoritable_id** | **str** | The FilTeam ID (as string to preserve precision) | 
**favorites_category_id** | **int** | Optional category to assign the favorite to | [optional] 

## Example

```python
from winthrop_client_python.models.create_team_schedule_favorite_request import CreateTeamScheduleFavoriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamScheduleFavoriteRequest from a JSON string
create_team_schedule_favorite_request_instance = CreateTeamScheduleFavoriteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTeamScheduleFavoriteRequest.to_json())

# convert the object into a dict
create_team_schedule_favorite_request_dict = create_team_schedule_favorite_request_instance.to_dict()
# create an instance of CreateTeamScheduleFavoriteRequest from a dict
create_team_schedule_favorite_request_from_dict = CreateTeamScheduleFavoriteRequest.from_dict(create_team_schedule_favorite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


