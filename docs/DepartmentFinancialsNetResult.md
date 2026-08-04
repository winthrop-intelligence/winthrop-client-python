# DepartmentFinancialsNetResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** |  | 
**rank** | **int** |  | 
**cohort_size** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_financials_net_result import DepartmentFinancialsNetResult

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsNetResult from a JSON string
department_financials_net_result_instance = DepartmentFinancialsNetResult.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsNetResult.to_json())

# convert the object into a dict
department_financials_net_result_dict = department_financials_net_result_instance.to_dict()
# create an instance of DepartmentFinancialsNetResult from a dict
department_financials_net_result_from_dict = DepartmentFinancialsNetResult.from_dict(department_financials_net_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


