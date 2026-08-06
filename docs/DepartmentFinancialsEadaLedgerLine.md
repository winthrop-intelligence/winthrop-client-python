# DepartmentFinancialsEadaLedgerLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**label** | **str** |  | 
**amount_cents** | **int** |  | 
**basis** | **str** | Reporting basis this figure was filed on | 
**comparable_with_frs** | **bool** | Always false for EADA lines — definitions differ from FRS, so the page must mark them rather than blend them with filed NCAA figures | 

## Example

```python
from winthrop_client_python.models.department_financials_eada_ledger_line import DepartmentFinancialsEadaLedgerLine

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsEadaLedgerLine from a JSON string
department_financials_eada_ledger_line_instance = DepartmentFinancialsEadaLedgerLine.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsEadaLedgerLine.to_json())

# convert the object into a dict
department_financials_eada_ledger_line_dict = department_financials_eada_ledger_line_instance.to_dict()
# create an instance of DepartmentFinancialsEadaLedgerLine from a dict
department_financials_eada_ledger_line_from_dict = DepartmentFinancialsEadaLedgerLine.from_dict(department_financials_eada_ledger_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


