# TeamSchedulePlayerDataTransfersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**eligible** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_player_data_transfers_inner import TeamSchedulePlayerDataTransfersInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSchedulePlayerDataTransfersInner from a JSON string
team_schedule_player_data_transfers_inner_instance = TeamSchedulePlayerDataTransfersInner.from_json(json)
# print the JSON string representation of the object
print(TeamSchedulePlayerDataTransfersInner.to_json())

# convert the object into a dict
team_schedule_player_data_transfers_inner_dict = team_schedule_player_data_transfers_inner_instance.to_dict()
# create an instance of TeamSchedulePlayerDataTransfersInner from a dict
team_schedule_player_data_transfers_inner_from_dict = TeamSchedulePlayerDataTransfersInner.from_dict(team_schedule_player_data_transfers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


