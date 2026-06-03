# CreateScheduleTournamentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_tournament** | [**CreateScheduleTournamentRequestScheduleTournament**](CreateScheduleTournamentRequestScheduleTournament.md) |  | 

## Example

```python
from winthrop_client_python.models.create_schedule_tournament_request import CreateScheduleTournamentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleTournamentRequest from a JSON string
create_schedule_tournament_request_instance = CreateScheduleTournamentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleTournamentRequest.to_json())

# convert the object into a dict
create_schedule_tournament_request_dict = create_schedule_tournament_request_instance.to_dict()
# create an instance of CreateScheduleTournamentRequest from a dict
create_schedule_tournament_request_from_dict = CreateScheduleTournamentRequest.from_dict(create_schedule_tournament_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


