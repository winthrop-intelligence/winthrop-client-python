# UpdateAdminSeasonStatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | [**UpdateAdminSeasonStatsRequestSeason**](UpdateAdminSeasonStatsRequestSeason.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_season_stats_request import UpdateAdminSeasonStatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminSeasonStatsRequest from a JSON string
update_admin_season_stats_request_instance = UpdateAdminSeasonStatsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminSeasonStatsRequest.to_json())

# convert the object into a dict
update_admin_season_stats_request_dict = update_admin_season_stats_request_instance.to_dict()
# create an instance of UpdateAdminSeasonStatsRequest from a dict
update_admin_season_stats_request_from_dict = UpdateAdminSeasonStatsRequest.from_dict(update_admin_season_stats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


