# RecordPositionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport** | **str** |  | 
**year_str** | **str** |  | 
**school_name** | **str** |  | 
**school_id** | **int** |  | 
**position_sport** | **str** |  | 
**record** | **str** |  | [optional] 
**rpi** | **str** |  | [optional] 
**net_rank** | **str** |  | [optional] 
**ap_rank** | **str** |  | [optional] 
**apr_asr** | **str** |  | [optional] 
**academic_metric** | **str** | The measure in apr_asr, selected using the same school division rule; null for administrator rows. | 
**coach_apr** | **float** |  | [optional] 
**departing** | **bool** |  | [optional] 
**head_coach** | **bool** | True when the position includes Head Coach or Interim Head Coach. | [optional] 
**assistant_coach** | **bool** | True when the position includes a coaching type in the Assistant Coaches group, excluding Offensive, Defensive and Special Teams Analysts. A season can be neither head coach nor assistant, e.g. an analyst or operations role. | [optional] 
**us_news** | **str** |  | [optional] 
**directors_cup** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.record_position_entry import RecordPositionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RecordPositionEntry from a JSON string
record_position_entry_instance = RecordPositionEntry.from_json(json)
# print the JSON string representation of the object
print(RecordPositionEntry.to_json())

# convert the object into a dict
record_position_entry_dict = record_position_entry_instance.to_dict()
# create an instance of RecordPositionEntry from a dict
record_position_entry_from_dict = RecordPositionEntry.from_dict(record_position_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


