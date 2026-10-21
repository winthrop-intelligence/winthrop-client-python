# UpdateAdminDealRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_note** | **str** | Optional reason, stored on every audit version; trimmed, blank means absent. | [optional] 
**deal** | [**UpdateAdminDealRequestDeal**](UpdateAdminDealRequestDeal.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_deal_request import UpdateAdminDealRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminDealRequest from a JSON string
update_admin_deal_request_instance = UpdateAdminDealRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminDealRequest.to_json())

# convert the object into a dict
update_admin_deal_request_dict = update_admin_deal_request_instance.to_dict()
# create an instance of UpdateAdminDealRequest from a dict
update_admin_deal_request_from_dict = UpdateAdminDealRequest.from_dict(update_admin_deal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


