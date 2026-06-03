# CreateScheduleTournamentRequestScheduleTournament


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | 
**var_date** | **date** |  | 
**name** | **str** | Tournament name (e.g. \&quot;Maui Invitational\&quot;). Trimmed before validation; must be 3–30 characters after trimming. | 

## Example

```python
from winthrop_client_python.models.create_schedule_tournament_request_schedule_tournament import CreateScheduleTournamentRequestScheduleTournament

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleTournamentRequestScheduleTournament from a JSON string
create_schedule_tournament_request_schedule_tournament_instance = CreateScheduleTournamentRequestScheduleTournament.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleTournamentRequestScheduleTournament.to_json())

# convert the object into a dict
create_schedule_tournament_request_schedule_tournament_dict = create_schedule_tournament_request_schedule_tournament_instance.to_dict()
# create an instance of CreateScheduleTournamentRequestScheduleTournament from a dict
create_schedule_tournament_request_schedule_tournament_from_dict = CreateScheduleTournamentRequestScheduleTournament.from_dict(create_schedule_tournament_request_schedule_tournament_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


