# CreateAdminDealRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_note** | **str** | Optional reason, stored on every audit version; trimmed, blank means absent. | [optional] 
**deal** | [**CreateAdminDealRequestDeal**](CreateAdminDealRequestDeal.md) |  | 

## Example

```python
from winthrop_client_python.models.create_admin_deal_request import CreateAdminDealRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminDealRequest from a JSON string
create_admin_deal_request_instance = CreateAdminDealRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminDealRequest.to_json())

# convert the object into a dict
create_admin_deal_request_dict = create_admin_deal_request_instance.to_dict()
# create an instance of CreateAdminDealRequest from a dict
create_admin_deal_request_from_dict = CreateAdminDealRequest.from_dict(create_admin_deal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


