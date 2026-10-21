# CreateAdminDealStatusesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal_status** | [**CreateAdminDealStatusesRequestDealStatus**](CreateAdminDealStatusesRequestDealStatus.md) |  | 

## Example

```python
from winthrop_client_python.models.create_admin_deal_statuses_request import CreateAdminDealStatusesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminDealStatusesRequest from a JSON string
create_admin_deal_statuses_request_instance = CreateAdminDealStatusesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminDealStatusesRequest.to_json())

# convert the object into a dict
create_admin_deal_statuses_request_dict = create_admin_deal_statuses_request_instance.to_dict()
# create an instance of CreateAdminDealStatusesRequest from a dict
create_admin_deal_statuses_request_from_dict = CreateAdminDealStatusesRequest.from_dict(create_admin_deal_statuses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


