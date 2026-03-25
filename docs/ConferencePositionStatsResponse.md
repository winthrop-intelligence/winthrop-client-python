# ConferencePositionStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sports** | [**List[PositionSportStat]**](PositionSportStat.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.conference_position_stats_response import ConferencePositionStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConferencePositionStatsResponse from a JSON string
conference_position_stats_response_instance = ConferencePositionStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ConferencePositionStatsResponse.to_json())

# convert the object into a dict
conference_position_stats_response_dict = conference_position_stats_response_instance.to_dict()
# create an instance of ConferencePositionStatsResponse from a dict
conference_position_stats_response_from_dict = ConferencePositionStatsResponse.from_dict(conference_position_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


