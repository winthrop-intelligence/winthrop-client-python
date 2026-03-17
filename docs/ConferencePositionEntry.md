# ConferencePositionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year_str** | **str** |  | 
**school_name** | **str** |  | 
**school_id** | **int** |  | 
**sport** | **str** |  | 
**position** | **str** |  | 
**record** | **str** |  | [optional] 
**conference_record** | **str** |  | [optional] 
**postseason** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.conference_position_entry import ConferencePositionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ConferencePositionEntry from a JSON string
conference_position_entry_instance = ConferencePositionEntry.from_json(json)
# print the JSON string representation of the object
print(ConferencePositionEntry.to_json())

# convert the object into a dict
conference_position_entry_dict = conference_position_entry_instance.to_dict()
# create an instance of ConferencePositionEntry from a dict
conference_position_entry_from_dict = ConferencePositionEntry.from_dict(conference_position_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


