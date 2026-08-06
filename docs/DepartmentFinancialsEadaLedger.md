# DepartmentFinancialsEadaLedger

The EADA ledger for a school. Public federal data, so it is present for private schools that file no FRS report. Lines the source does not report are omitted rather than returned as zero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**basis** | **str** |  | 
**comparable_with_frs** | **bool** |  | 
**lines** | [**List[DepartmentFinancialsEadaLedgerLine]**](DepartmentFinancialsEadaLedgerLine.md) |  | 

## Example

```python
from winthrop_client_python.models.department_financials_eada_ledger import DepartmentFinancialsEadaLedger

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsEadaLedger from a JSON string
department_financials_eada_ledger_instance = DepartmentFinancialsEadaLedger.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsEadaLedger.to_json())

# convert the object into a dict
department_financials_eada_ledger_dict = department_financials_eada_ledger_instance.to_dict()
# create an instance of DepartmentFinancialsEadaLedger from a dict
department_financials_eada_ledger_from_dict = DepartmentFinancialsEadaLedger.from_dict(department_financials_eada_ledger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


