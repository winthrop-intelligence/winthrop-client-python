# UpdateTeamScheduleFavoriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorites_category_id** | **int** | The category to move this favorite to | [optional] 

## Example

```python
from winthrop_client_python.models.update_team_schedule_favorite_request import UpdateTeamScheduleFavoriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamScheduleFavoriteRequest from a JSON string
update_team_schedule_favorite_request_instance = UpdateTeamScheduleFavoriteRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTeamScheduleFavoriteRequest.to_json())

# convert the object into a dict
update_team_schedule_favorite_request_dict = update_team_schedule_favorite_request_instance.to_dict()
# create an instance of UpdateTeamScheduleFavoriteRequest from a dict
update_team_schedule_favorite_request_from_dict = UpdateTeamScheduleFavoriteRequest.from_dict(update_team_schedule_favorite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


