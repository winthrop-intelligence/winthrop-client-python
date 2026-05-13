# CashflowEntry

Per-school cashflow record backing an aggregate stat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | **str** |  | [optional] 
**amount** | **float** | Cashflow amount in dollars | [optional] 

## Example

```python
from winthrop_client_python.models.cashflow_entry import CashflowEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowEntry from a JSON string
cashflow_entry_instance = CashflowEntry.from_json(json)
# print the JSON string representation of the object
print(CashflowEntry.to_json())

# convert the object into a dict
cashflow_entry_dict = cashflow_entry_instance.to_dict()
# create an instance of CashflowEntry from a dict
cashflow_entry_from_dict = CashflowEntry.from_dict(cashflow_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


