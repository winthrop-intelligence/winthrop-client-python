# AdminArchiveTransferRequestErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **Dict[str, List[str]]** |  | 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_request_errors import AdminArchiveTransferRequestErrors

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferRequestErrors from a JSON string
admin_archive_transfer_request_errors_instance = AdminArchiveTransferRequestErrors.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferRequestErrors.to_json())

# convert the object into a dict
admin_archive_transfer_request_errors_dict = admin_archive_transfer_request_errors_instance.to_dict()
# create an instance of AdminArchiveTransferRequestErrors from a dict
admin_archive_transfer_request_errors_from_dict = AdminArchiveTransferRequestErrors.from_dict(admin_archive_transfer_request_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


