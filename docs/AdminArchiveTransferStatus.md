# AdminArchiveTransferStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**worker** | [**AdminArchiveTransferStatusWorker**](AdminArchiveTransferStatusWorker.md) |  | 
**limits** | [**AdminArchiveTransferStatusLimits**](AdminArchiveTransferStatusLimits.md) |  | 
**tables** | [**List[AdminArchiveTransferTable]**](AdminArchiveTransferTable.md) |  | 
**requests** | [**List[AdminArchiveTransferRequest]**](AdminArchiveTransferRequest.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_status import AdminArchiveTransferStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferStatus from a JSON string
admin_archive_transfer_status_instance = AdminArchiveTransferStatus.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferStatus.to_json())

# convert the object into a dict
admin_archive_transfer_status_dict = admin_archive_transfer_status_instance.to_dict()
# create an instance of AdminArchiveTransferStatus from a dict
admin_archive_transfer_status_from_dict = AdminArchiveTransferStatus.from_dict(admin_archive_transfer_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


