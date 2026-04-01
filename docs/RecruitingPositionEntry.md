# RecruitingPositionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport** | **str** |  | 
**year_str** | **str** |  | 
**school_name** | **str** |  | 
**school_id** | **int** |  | 
**class_rank** | **int** |  | [optional] 
**record** | **str** |  | [optional] 
**conference_record** | **str** |  | [optional] 
**recruiting_budget_cents** | **int** |  | [optional] 
**sport_budget_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.recruiting_position_entry import RecruitingPositionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RecruitingPositionEntry from a JSON string
recruiting_position_entry_instance = RecruitingPositionEntry.from_json(json)
# print the JSON string representation of the object
print(RecruitingPositionEntry.to_json())

# convert the object into a dict
recruiting_position_entry_dict = recruiting_position_entry_instance.to_dict()
# create an instance of RecruitingPositionEntry from a dict
recruiting_position_entry_from_dict = RecruitingPositionEntry.from_dict(recruiting_position_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


