# CompensationComparisonCompVisibility

Class-level capability flags: whether the caller's account can see coach / administrator compensation at all, and whether administrator records were searched. Per-row visibility is carried by each row's comp_status (comp_redacted) and the cohort comp_redacted_count.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_compensation** | **bool** |  | 
**administrator_compensation** | **bool** |  | 
**administrator_records_searched** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.compensation_comparison_comp_visibility import CompensationComparisonCompVisibility

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationComparisonCompVisibility from a JSON string
compensation_comparison_comp_visibility_instance = CompensationComparisonCompVisibility.from_json(json)
# print the JSON string representation of the object
print(CompensationComparisonCompVisibility.to_json())

# convert the object into a dict
compensation_comparison_comp_visibility_dict = compensation_comparison_comp_visibility_instance.to_dict()
# create an instance of CompensationComparisonCompVisibility from a dict
compensation_comparison_comp_visibility_from_dict = CompensationComparisonCompVisibility.from_dict(compensation_comparison_comp_visibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


