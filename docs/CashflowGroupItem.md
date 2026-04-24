# CashflowGroupItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_id** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.cashflow_group_item import CashflowGroupItem

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowGroupItem from a JSON string
cashflow_group_item_instance = CashflowGroupItem.from_json(json)
# print the JSON string representation of the object
print(CashflowGroupItem.to_json())

# convert the object into a dict
cashflow_group_item_dict = cashflow_group_item_instance.to_dict()
# create an instance of CashflowGroupItem from a dict
cashflow_group_item_from_dict = CashflowGroupItem.from_dict(cashflow_group_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


