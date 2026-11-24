# AdminArchiveTransferRequestRequestedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_request_requested_by import AdminArchiveTransferRequestRequestedBy

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferRequestRequestedBy from a JSON string
admin_archive_transfer_request_requested_by_instance = AdminArchiveTransferRequestRequestedBy.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferRequestRequestedBy.to_json())

# convert the object into a dict
admin_archive_transfer_request_requested_by_dict = admin_archive_transfer_request_requested_by_instance.to_dict()
# create an instance of AdminArchiveTransferRequestRequestedBy from a dict
admin_archive_transfer_request_requested_by_from_dict = AdminArchiveTransferRequestRequestedBy.from_dict(admin_archive_transfer_request_requested_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


