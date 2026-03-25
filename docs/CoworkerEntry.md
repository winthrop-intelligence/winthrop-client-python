# CoworkerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**name** | **str** |  | 
**initials** | **str** |  | 
**avatar_url** | **str** |  | [optional] 
**position_type_name** | **str** |  | [optional] 
**start_year** | **int** |  | 
**end_year** | **int** |  | 
**current_position_title** | **str** |  | [optional] 
**current_school_name** | **str** |  | [optional] 
**salary_cents** | **int** |  | [optional] 
**coach_friendly_id** | **str** |  | 

## Example

```python
from winthrop_client_python.models.coworker_entry import CoworkerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CoworkerEntry from a JSON string
coworker_entry_instance = CoworkerEntry.from_json(json)
# print the JSON string representation of the object
print(CoworkerEntry.to_json())

# convert the object into a dict
coworker_entry_dict = coworker_entry_instance.to_dict()
# create an instance of CoworkerEntry from a dict
coworker_entry_from_dict = CoworkerEntry.from_dict(coworker_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


