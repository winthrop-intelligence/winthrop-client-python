# MassUpdateAdminRequestedItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | IDs of the requested items to update. | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.mass_update_admin_requested_items_request import MassUpdateAdminRequestedItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassUpdateAdminRequestedItemsRequest from a JSON string
mass_update_admin_requested_items_request_instance = MassUpdateAdminRequestedItemsRequest.from_json(json)
# print the JSON string representation of the object
print(MassUpdateAdminRequestedItemsRequest.to_json())

# convert the object into a dict
mass_update_admin_requested_items_request_dict = mass_update_admin_requested_items_request_instance.to_dict()
# create an instance of MassUpdateAdminRequestedItemsRequest from a dict
mass_update_admin_requested_items_request_from_dict = MassUpdateAdminRequestedItemsRequest.from_dict(mass_update_admin_requested_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


