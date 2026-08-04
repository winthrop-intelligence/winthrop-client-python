# DepartmentFinancialsLedgerLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**label** | **str** |  | 
**amount_cents** | **int** |  | 
**highlight** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.department_financials_ledger_line import DepartmentFinancialsLedgerLine

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsLedgerLine from a JSON string
department_financials_ledger_line_instance = DepartmentFinancialsLedgerLine.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsLedgerLine.to_json())

# convert the object into a dict
department_financials_ledger_line_dict = department_financials_ledger_line_instance.to_dict()
# create an instance of DepartmentFinancialsLedgerLine from a dict
department_financials_ledger_line_from_dict = DepartmentFinancialsLedgerLine.from_dict(department_financials_ledger_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


