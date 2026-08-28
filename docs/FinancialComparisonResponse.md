# FinancialComparisonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**grain** | **str** |  | 
**requested_year** | **int** |  | 
**metric** | **str** |  | 
**schools** | [**List[FinancialComparisonSchoolEntry]**](FinancialComparisonSchoolEntry.md) |  | 
**comparison** | [**FinancialComparison**](FinancialComparison.md) |  | 

## Example

```python
from winthrop_client_python.models.financial_comparison_response import FinancialComparisonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialComparisonResponse from a JSON string
financial_comparison_response_instance = FinancialComparisonResponse.from_json(json)
# print the JSON string representation of the object
print(FinancialComparisonResponse.to_json())

# convert the object into a dict
financial_comparison_response_dict = financial_comparison_response_instance.to_dict()
# create an instance of FinancialComparisonResponse from a dict
financial_comparison_response_from_dict = FinancialComparisonResponse.from_dict(financial_comparison_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


