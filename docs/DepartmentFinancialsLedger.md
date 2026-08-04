# DepartmentFinancialsLedger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_cents** | **int** |  | 
**lines** | [**List[DepartmentFinancialsLedgerLine]**](DepartmentFinancialsLedgerLine.md) |  | 

## Example

```python
from winthrop_client_python.models.department_financials_ledger import DepartmentFinancialsLedger

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsLedger from a JSON string
department_financials_ledger_instance = DepartmentFinancialsLedger.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsLedger.to_json())

# convert the object into a dict
department_financials_ledger_dict = department_financials_ledger_instance.to_dict()
# create an instance of DepartmentFinancialsLedger from a dict
department_financials_ledger_from_dict = DepartmentFinancialsLedger.from_dict(department_financials_ledger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


