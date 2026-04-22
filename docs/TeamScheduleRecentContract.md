# TeamScheduleRecentContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_name** | **str** |  | [optional] 
**game_contract_id** | **int** |  | [optional] 
**year** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_recent_contract import TeamScheduleRecentContract

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleRecentContract from a JSON string
team_schedule_recent_contract_instance = TeamScheduleRecentContract.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleRecentContract.to_json())

# convert the object into a dict
team_schedule_recent_contract_dict = team_schedule_recent_contract_instance.to_dict()
# create an instance of TeamScheduleRecentContract from a dict
team_schedule_recent_contract_from_dict = TeamScheduleRecentContract.from_dict(team_schedule_recent_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


