# UpdateAdminDealStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal_status** | [**UpdateAdminDealStatusRequestDealStatus**](UpdateAdminDealStatusRequestDealStatus.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_deal_status_request import UpdateAdminDealStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminDealStatusRequest from a JSON string
update_admin_deal_status_request_instance = UpdateAdminDealStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminDealStatusRequest.to_json())

# convert the object into a dict
update_admin_deal_status_request_dict = update_admin_deal_status_request_instance.to_dict()
# create an instance of UpdateAdminDealStatusRequest from a dict
update_admin_deal_status_request_from_dict = UpdateAdminDealStatusRequest.from_dict(update_admin_deal_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


