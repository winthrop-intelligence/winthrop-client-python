# CompensationComparisonResolvedScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schools** | [**List[CompensationComparisonResolvedScopeSchoolsInner]**](CompensationComparisonResolvedScopeSchoolsInner.md) |  | 
**unresolved_school_ids** | **List[int]** |  | 
**conference** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 
**sport** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 
**position_type** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 
**year** | **int** |  | 
**title_include** | **List[str]** |  | 
**title_exclude** | **List[str]** |  | 
**include_missing** | **bool** |  | 
**per_school_limit** | **int** |  | 
**max_rows** | **int** |  | 
**truncated** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.compensation_comparison_resolved_scope import CompensationComparisonResolvedScope

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationComparisonResolvedScope from a JSON string
compensation_comparison_resolved_scope_instance = CompensationComparisonResolvedScope.from_json(json)
# print the JSON string representation of the object
print(CompensationComparisonResolvedScope.to_json())

# convert the object into a dict
compensation_comparison_resolved_scope_dict = compensation_comparison_resolved_scope_instance.to_dict()
# create an instance of CompensationComparisonResolvedScope from a dict
compensation_comparison_resolved_scope_from_dict = CompensationComparisonResolvedScope.from_dict(compensation_comparison_resolved_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


