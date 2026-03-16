# TeamScheduleDetailSport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_detail_sport import TeamScheduleDetailSport

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleDetailSport from a JSON string
team_schedule_detail_sport_instance = TeamScheduleDetailSport.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleDetailSport.to_json())

# convert the object into a dict
team_schedule_detail_sport_dict = team_schedule_detail_sport_instance.to_dict()
# create an instance of TeamScheduleDetailSport from a dict
team_schedule_detail_sport_from_dict = TeamScheduleDetailSport.from_dict(team_schedule_detail_sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


