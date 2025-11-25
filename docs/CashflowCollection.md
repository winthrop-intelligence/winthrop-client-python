# CashflowCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Cashflow]**](Cashflow.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.cashflow_collection import CashflowCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowCollection from a JSON string
cashflow_collection_instance = CashflowCollection.from_json(json)
# print the JSON string representation of the object
print(CashflowCollection.to_json())

# convert the object into a dict
cashflow_collection_dict = cashflow_collection_instance.to_dict()
# create an instance of CashflowCollection from a dict
cashflow_collection_from_dict = CashflowCollection.from_dict(cashflow_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


