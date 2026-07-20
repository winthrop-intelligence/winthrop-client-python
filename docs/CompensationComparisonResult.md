# CompensationComparisonResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolved_scope** | [**CompensationComparisonResolvedScope**](CompensationComparisonResolvedScope.md) |  | 
**rows** | [**List[CompensationComparisonRow]**](CompensationComparisonRow.md) |  | 
**cohort_stats** | [**CompensationComparisonCohortStats**](CompensationComparisonCohortStats.md) |  | 
**comp_visibility** | [**CompensationComparisonCompVisibility**](CompensationComparisonCompVisibility.md) |  | 
**warnings** | **List[str]** |  | 

## Example

```python
from winthrop_client_python.models.compensation_comparison_result import CompensationComparisonResult

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationComparisonResult from a JSON string
compensation_comparison_result_instance = CompensationComparisonResult.from_json(json)
# print the JSON string representation of the object
print(CompensationComparisonResult.to_json())

# convert the object into a dict
compensation_comparison_result_dict = compensation_comparison_result_instance.to_dict()
# create an instance of CompensationComparisonResult from a dict
compensation_comparison_result_from_dict = CompensationComparisonResult.from_dict(compensation_comparison_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


