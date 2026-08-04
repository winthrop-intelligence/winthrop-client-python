# DepartmentFinancialsTrendEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**exp_total_cents** | **int** |  | 
**rev_total_cents** | **int** |  | 
**provisional** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.department_financials_trend_entry import DepartmentFinancialsTrendEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsTrendEntry from a JSON string
department_financials_trend_entry_instance = DepartmentFinancialsTrendEntry.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsTrendEntry.to_json())

# convert the object into a dict
department_financials_trend_entry_dict = department_financials_trend_entry_instance.to_dict()
# create an instance of DepartmentFinancialsTrendEntry from a dict
department_financials_trend_entry_from_dict = DepartmentFinancialsTrendEntry.from_dict(department_financials_trend_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


