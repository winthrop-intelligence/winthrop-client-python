# DealUpdateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**deal_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**deal_type_name** | **str** |  | [optional] 
**deal_type_id** | **int** |  | [optional] 
**vendor_names** | **List[str]** |  | [optional] 
**start_year** | **int** |  | [optional] 
**end_year** | **int** |  | [optional] 
**start_at** | **datetime** |  | [optional] 
**end_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**summary** | **str** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**vendors** | [**List[DealDetailVendor]**](DealDetailVendor.md) |  | [optional] 
**deal_detail** | [**DealUpdateDetail**](DealUpdateDetail.md) |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.deal_update_result import DealUpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of DealUpdateResult from a JSON string
deal_update_result_instance = DealUpdateResult.from_json(json)
# print the JSON string representation of the object
print(DealUpdateResult.to_json())

# convert the object into a dict
deal_update_result_dict = deal_update_result_instance.to_dict()
# create an instance of DealUpdateResult from a dict
deal_update_result_from_dict = DealUpdateResult.from_dict(deal_update_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


