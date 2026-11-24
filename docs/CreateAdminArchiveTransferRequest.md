# CreateAdminArchiveTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_transfer_request** | [**CreateAdminArchiveTransferRequestArchiveTransferRequest**](CreateAdminArchiveTransferRequestArchiveTransferRequest.md) |  | 

## Example

```python
from winthrop_client_python.models.create_admin_archive_transfer_request import CreateAdminArchiveTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminArchiveTransferRequest from a JSON string
create_admin_archive_transfer_request_instance = CreateAdminArchiveTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminArchiveTransferRequest.to_json())

# convert the object into a dict
create_admin_archive_transfer_request_dict = create_admin_archive_transfer_request_instance.to_dict()
# create an instance of CreateAdminArchiveTransferRequest from a dict
create_admin_archive_transfer_request_from_dict = CreateAdminArchiveTransferRequest.from_dict(create_admin_archive_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


