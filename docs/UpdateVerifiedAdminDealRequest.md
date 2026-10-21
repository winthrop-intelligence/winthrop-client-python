# UpdateVerifiedAdminDealRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_note** | **str** | Optional reason, stored on every audit version; trimmed, blank means absent. | [optional] 
**deal** | [**UpdateVerifiedAdminDealRequestDeal**](UpdateVerifiedAdminDealRequestDeal.md) |  | 

## Example

```python
from winthrop_client_python.models.update_verified_admin_deal_request import UpdateVerifiedAdminDealRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVerifiedAdminDealRequest from a JSON string
update_verified_admin_deal_request_instance = UpdateVerifiedAdminDealRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateVerifiedAdminDealRequest.to_json())

# convert the object into a dict
update_verified_admin_deal_request_dict = update_verified_admin_deal_request_instance.to_dict()
# create an instance of UpdateVerifiedAdminDealRequest from a dict
update_verified_admin_deal_request_from_dict = UpdateVerifiedAdminDealRequest.from_dict(update_verified_admin_deal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


