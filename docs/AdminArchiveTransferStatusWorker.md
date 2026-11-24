# AdminArchiveTransferStatusWorker

The archive copy job's last check-in; null when it has never checked in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checked_at** | **datetime** |  | 
**copy_enabled** | **bool** |  | 
**writer_configured** | **bool** |  | 
**stale** | **bool** | Not checked in for 15 minutes | 
**ready** | **bool** | A request made now will be run | 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_status_worker import AdminArchiveTransferStatusWorker

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferStatusWorker from a JSON string
admin_archive_transfer_status_worker_instance = AdminArchiveTransferStatusWorker.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferStatusWorker.to_json())

# convert the object into a dict
admin_archive_transfer_status_worker_dict = admin_archive_transfer_status_worker_instance.to_dict()
# create an instance of AdminArchiveTransferStatusWorker from a dict
admin_archive_transfer_status_worker_from_dict = AdminArchiveTransferStatusWorker.from_dict(admin_archive_transfer_status_worker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


