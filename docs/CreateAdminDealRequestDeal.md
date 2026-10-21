# CreateAdminDealRequestDeal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**deal_type_id** | **int** |  | [optional] 
**start_at** | **datetime** |  | [optional] 
**end_at** | **datetime** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**vendor_ids** | **List[int]** |  | [optional] 
**raw_contract_attributes** | [**CreateAdminDealRequestDealRawContractAttributes**](CreateAdminDealRequestDealRawContractAttributes.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_deal_request_deal import CreateAdminDealRequestDeal

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminDealRequestDeal from a JSON string
create_admin_deal_request_deal_instance = CreateAdminDealRequestDeal.from_json(json)
# print the JSON string representation of the object
print(CreateAdminDealRequestDeal.to_json())

# convert the object into a dict
create_admin_deal_request_deal_dict = create_admin_deal_request_deal_instance.to_dict()
# create an instance of CreateAdminDealRequestDeal from a dict
create_admin_deal_request_deal_from_dict = CreateAdminDealRequestDeal.from_dict(create_admin_deal_request_deal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


