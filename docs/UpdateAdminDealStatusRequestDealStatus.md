# UpdateAdminDealStatusRequestDealStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal_status_type_id** | **int** |  | [optional] 
**deal_source_id** | **int** |  | [optional] 
**source_note** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**auto_renew** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_deal_status_request_deal_status import UpdateAdminDealStatusRequestDealStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminDealStatusRequestDealStatus from a JSON string
update_admin_deal_status_request_deal_status_instance = UpdateAdminDealStatusRequestDealStatus.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminDealStatusRequestDealStatus.to_json())

# convert the object into a dict
update_admin_deal_status_request_deal_status_dict = update_admin_deal_status_request_deal_status_instance.to_dict()
# create an instance of UpdateAdminDealStatusRequestDealStatus from a dict
update_admin_deal_status_request_deal_status_from_dict = UpdateAdminDealStatusRequestDealStatus.from_dict(update_admin_deal_status_request_deal_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


