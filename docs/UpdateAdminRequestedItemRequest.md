# UpdateAdminRequestedItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_item** | [**UpdateAdminRequestedItemRequestRequestedItem**](UpdateAdminRequestedItemRequestRequestedItem.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_requested_item_request import UpdateAdminRequestedItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminRequestedItemRequest from a JSON string
update_admin_requested_item_request_instance = UpdateAdminRequestedItemRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminRequestedItemRequest.to_json())

# convert the object into a dict
update_admin_requested_item_request_dict = update_admin_requested_item_request_instance.to_dict()
# create an instance of UpdateAdminRequestedItemRequest from a dict
update_admin_requested_item_request_from_dict = UpdateAdminRequestedItemRequest.from_dict(update_admin_requested_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


