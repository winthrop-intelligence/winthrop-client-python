# CreateAdminArchiveTransferRequestArchiveTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** |  | 
**max_rows** | **int** |  | 
**max_minutes** | **int** |  | 

## Example

```python
from winthrop_client_python.models.create_admin_archive_transfer_request_archive_transfer_request import CreateAdminArchiveTransferRequestArchiveTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminArchiveTransferRequestArchiveTransferRequest from a JSON string
create_admin_archive_transfer_request_archive_transfer_request_instance = CreateAdminArchiveTransferRequestArchiveTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminArchiveTransferRequestArchiveTransferRequest.to_json())

# convert the object into a dict
create_admin_archive_transfer_request_archive_transfer_request_dict = create_admin_archive_transfer_request_archive_transfer_request_instance.to_dict()
# create an instance of CreateAdminArchiveTransferRequestArchiveTransferRequest from a dict
create_admin_archive_transfer_request_archive_transfer_request_from_dict = CreateAdminArchiveTransferRequestArchiveTransferRequest.from_dict(create_admin_archive_transfer_request_archive_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


