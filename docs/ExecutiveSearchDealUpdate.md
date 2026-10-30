# ExecutiveSearchDealUpdate

Executive Search deals (WINAD-10742). Every field is optional and null clears it; blank means not stated, never 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **int** | Id of an existing position (the role being filled); anything else is refused with 422 &#x60;deal_detail.position_id&#x60;. | [optional] 
**search_scope** | **str** |  | [optional] 
**search_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**fee_basis** | **str** |  | [optional] 
**fee_percent** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**guarantee_months** | [**DealUpdateMonths**](DealUpdateMonths.md) |  | [optional] 
**expense_terms** | **str** |  | [optional] 
**annual_retainer** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.executive_search_deal_update import ExecutiveSearchDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutiveSearchDealUpdate from a JSON string
executive_search_deal_update_instance = ExecutiveSearchDealUpdate.from_json(json)
# print the JSON string representation of the object
print(ExecutiveSearchDealUpdate.to_json())

# convert the object into a dict
executive_search_deal_update_dict = executive_search_deal_update_instance.to_dict()
# create an instance of ExecutiveSearchDealUpdate from a dict
executive_search_deal_update_from_dict = ExecutiveSearchDealUpdate.from_dict(executive_search_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


