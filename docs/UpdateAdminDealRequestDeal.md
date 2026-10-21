# UpdateAdminDealRequestDeal


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
**raw_contract_attributes** | [**UpdateAdminDealRequestDealRawContractAttributes**](UpdateAdminDealRequestDealRawContractAttributes.md) |  | [optional] 
**deal_detail_attributes** | **object** | Dynamic - real columns depend on the deal&#39;s deal_type (see AdminDealsOptions.deal_types[].deal_detail_fields) | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_deal_request_deal import UpdateAdminDealRequestDeal

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminDealRequestDeal from a JSON string
update_admin_deal_request_deal_instance = UpdateAdminDealRequestDeal.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminDealRequestDeal.to_json())

# convert the object into a dict
update_admin_deal_request_deal_dict = update_admin_deal_request_deal_instance.to_dict()
# create an instance of UpdateAdminDealRequestDeal from a dict
update_admin_deal_request_deal_from_dict = UpdateAdminDealRequestDeal.from_dict(update_admin_deal_request_deal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


