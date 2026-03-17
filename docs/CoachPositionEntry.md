# CoachPositionEntry


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

## Example

```python
from winthrop_client_python.models.coach_position_entry import CoachPositionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CoachPositionEntry from a JSON string
coach_position_entry_instance = CoachPositionEntry.from_json(json)
# print the JSON string representation of the object
print(CoachPositionEntry.to_json())

# convert the object into a dict
coach_position_entry_dict = coach_position_entry_instance.to_dict()
# create an instance of CoachPositionEntry from a dict
coach_position_entry_from_dict = CoachPositionEntry.from_dict(coach_position_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


