# CoachRecordTab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leader_ad** | **bool** |  | 
**show_coach_apr** | **bool** |  | 
**positions** | [**List[RecordPositionEntry]**](RecordPositionEntry.md) |  | 
**conference_positions** | [**List[ConferencePositionEntry]**](ConferencePositionEntry.md) |  | 
**performance_chart** | [**PerformanceChartData**](PerformanceChartData.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_record_tab import CoachRecordTab

# TODO update the JSON string below
json = "{}"
# create an instance of CoachRecordTab from a JSON string
coach_record_tab_instance = CoachRecordTab.from_json(json)
# print the JSON string representation of the object
print(CoachRecordTab.to_json())

# convert the object into a dict
coach_record_tab_dict = coach_record_tab_instance.to_dict()
# create an instance of CoachRecordTab from a dict
coach_record_tab_from_dict = CoachRecordTab.from_dict(coach_record_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


