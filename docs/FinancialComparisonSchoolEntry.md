# FinancialComparisonSchoolEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**school_name** | **str** |  | 
**results** | [**List[FinancialSelectionResult]**](FinancialSelectionResult.md) |  | 

## Example

```python
from winthrop_client_python.models.financial_comparison_school_entry import FinancialComparisonSchoolEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialComparisonSchoolEntry from a JSON string
financial_comparison_school_entry_instance = FinancialComparisonSchoolEntry.from_json(json)
# print the JSON string representation of the object
print(FinancialComparisonSchoolEntry.to_json())

# convert the object into a dict
financial_comparison_school_entry_dict = financial_comparison_school_entry_instance.to_dict()
# create an instance of FinancialComparisonSchoolEntry from a dict
financial_comparison_school_entry_from_dict = FinancialComparisonSchoolEntry.from_dict(financial_comparison_school_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


