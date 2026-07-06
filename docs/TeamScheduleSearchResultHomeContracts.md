# TeamScheduleSearchResultHomeContracts

Guarantee contracts where the school is the home/paying side, limited to contracts the caller can view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_paid_cents** | **int** | Mean comp_cents of the school&#39;s last 10 signed Guarantee contracts as the home side, excluding zero/blank comp. | [optional] 
**recent** | [**List[TeamScheduleRecentContract]**](TeamScheduleRecentContract.md) | Up to 3 most recent past-dated single-game Guarantee contracts (series excluded), newest first. | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_search_result_home_contracts import TeamScheduleSearchResultHomeContracts

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleSearchResultHomeContracts from a JSON string
team_schedule_search_result_home_contracts_instance = TeamScheduleSearchResultHomeContracts.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleSearchResultHomeContracts.to_json())

# convert the object into a dict
team_schedule_search_result_home_contracts_dict = team_schedule_search_result_home_contracts_instance.to_dict()
# create an instance of TeamScheduleSearchResultHomeContracts from a dict
team_schedule_search_result_home_contracts_from_dict = TeamScheduleSearchResultHomeContracts.from_dict(team_schedule_search_result_home_contracts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


