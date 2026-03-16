# TeamScheduleSearchResultAwayContracts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_received_cents** | **int** |  | [optional] 
**recent** | [**List[TeamScheduleRecentContract]**](TeamScheduleRecentContract.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_search_result_away_contracts import TeamScheduleSearchResultAwayContracts

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleSearchResultAwayContracts from a JSON string
team_schedule_search_result_away_contracts_instance = TeamScheduleSearchResultAwayContracts.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleSearchResultAwayContracts.to_json())

# convert the object into a dict
team_schedule_search_result_away_contracts_dict = team_schedule_search_result_away_contracts_instance.to_dict()
# create an instance of TeamScheduleSearchResultAwayContracts from a dict
team_schedule_search_result_away_contracts_from_dict = TeamScheduleSearchResultAwayContracts.from_dict(team_schedule_search_result_away_contracts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


