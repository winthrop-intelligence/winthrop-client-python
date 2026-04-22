# RecruitingBudgetEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_name** | **str** |  | 
**school_id** | **int** |  | 
**budget_cents** | **int** |  | [optional] 
**class_rank** | **int** |  | [optional] 
**conference_record** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.recruiting_budget_entry import RecruitingBudgetEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RecruitingBudgetEntry from a JSON string
recruiting_budget_entry_instance = RecruitingBudgetEntry.from_json(json)
# print the JSON string representation of the object
print(RecruitingBudgetEntry.to_json())

# convert the object into a dict
recruiting_budget_entry_dict = recruiting_budget_entry_instance.to_dict()
# create an instance of RecruitingBudgetEntry from a dict
recruiting_budget_entry_from_dict = RecruitingBudgetEntry.from_dict(recruiting_budget_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


