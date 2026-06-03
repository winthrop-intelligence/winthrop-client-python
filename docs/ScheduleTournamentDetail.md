# ScheduleTournamentDetail

A private /schedules grid multi-team event (MTE) placeholder (WINAD-9818). Distinct from Game (no opponent FK — opponents may be unknown when the event is added) and from ScheduleIntent (availability markers). One row per (school, sport, date).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**var_date** | **date** |  | [optional] 
**name** | **str** | Tournament name (e.g. \&quot;Maui Invitational\&quot;) | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_tournament_detail import ScheduleTournamentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTournamentDetail from a JSON string
schedule_tournament_detail_instance = ScheduleTournamentDetail.from_json(json)
# print the JSON string representation of the object
print(ScheduleTournamentDetail.to_json())

# convert the object into a dict
schedule_tournament_detail_dict = schedule_tournament_detail_instance.to_dict()
# create an instance of ScheduleTournamentDetail from a dict
schedule_tournament_detail_from_dict = ScheduleTournamentDetail.from_dict(schedule_tournament_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


