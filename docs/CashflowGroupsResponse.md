# CashflowGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revenues** | [**List[CashflowGroupItem]**](CashflowGroupItem.md) |  | [optional] 
**expenses** | [**List[CashflowGroupItem]**](CashflowGroupItem.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.cashflow_groups_response import CashflowGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowGroupsResponse from a JSON string
cashflow_groups_response_instance = CashflowGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(CashflowGroupsResponse.to_json())

# convert the object into a dict
cashflow_groups_response_dict = cashflow_groups_response_instance.to_dict()
# create an instance of CashflowGroupsResponse from a dict
cashflow_groups_response_from_dict = CashflowGroupsResponse.from_dict(cashflow_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


