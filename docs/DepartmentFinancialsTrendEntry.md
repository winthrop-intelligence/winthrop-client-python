# DepartmentFinancialsTrendEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**exp_total_cents** | **int** |  | 
**rev_total_cents** | **int** |  | 
**provisional** | **bool** |  | 
**basis** | **str** | Which report this year&#39;s figures were read from — the quadrant points&#39; vocabulary — so the chart labels every year by its own filing (WINAD-10400). Null on a year the school did not file. | 

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


