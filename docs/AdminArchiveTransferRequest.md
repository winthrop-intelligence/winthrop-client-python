# AdminArchiveTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**table_name** | **str** | null means every archive table, one after another | 
**max_rows** | **int** | At most this many rows per table | 
**max_minutes** | **int** | At most this many minutes for the whole request | 
**state** | **str** |  | 
**outcome** | **str** |  | [optional] 
**results** | [**Dict[str, AdminArchiveTransferRequestResultsValue]**](AdminArchiveTransferRequestResultsValue.md) | Per table, the run it worked on and how it ended | 
**stop_requested_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**error_message** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**requested_by** | [**AdminArchiveTransferRequestRequestedBy**](AdminArchiveTransferRequestRequestedBy.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_request import AdminArchiveTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferRequest from a JSON string
admin_archive_transfer_request_instance = AdminArchiveTransferRequest.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferRequest.to_json())

# convert the object into a dict
admin_archive_transfer_request_dict = admin_archive_transfer_request_instance.to_dict()
# create an instance of AdminArchiveTransferRequest from a dict
admin_archive_transfer_request_from_dict = AdminArchiveTransferRequest.from_dict(admin_archive_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


