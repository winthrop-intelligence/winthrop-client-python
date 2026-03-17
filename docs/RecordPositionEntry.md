# RecordPositionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year_str** | **str** |  | 
**school_name** | **str** |  | 
**school_id** | **int** |  | 
**position_sport** | **str** |  | 
**record** | **str** |  | [optional] 
**rpi** | **str** |  | [optional] 
**apr_asr** | **str** |  | [optional] 
**coach_apr** | **float** |  | [optional] 
**departing** | **bool** |  | [optional] 
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


