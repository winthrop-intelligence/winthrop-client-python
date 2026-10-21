# CreateAdminDealStatusesRequestDealStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**deal_type_id** | **int** |  | 
**deal_status_type_id** | **int** |  | [optional] 
**deal_source_id** | **int** |  | [optional] 
**source_note** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**auto_renew** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_deal_statuses_request_deal_status import CreateAdminDealStatusesRequestDealStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminDealStatusesRequestDealStatus from a JSON string
create_admin_deal_statuses_request_deal_status_instance = CreateAdminDealStatusesRequestDealStatus.from_json(json)
# print the JSON string representation of the object
print(CreateAdminDealStatusesRequestDealStatus.to_json())

# convert the object into a dict
create_admin_deal_statuses_request_deal_status_dict = create_admin_deal_statuses_request_deal_status_instance.to_dict()
# create an instance of CreateAdminDealStatusesRequestDealStatus from a dict
create_admin_deal_statuses_request_deal_status_from_dict = CreateAdminDealStatusesRequestDealStatus.from_dict(create_admin_deal_statuses_request_deal_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


