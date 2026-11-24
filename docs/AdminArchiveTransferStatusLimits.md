# AdminArchiveTransferStatusLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_rows** | **int** |  | 
**max_minutes** | **int** |  | 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_status_limits import AdminArchiveTransferStatusLimits

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferStatusLimits from a JSON string
admin_archive_transfer_status_limits_instance = AdminArchiveTransferStatusLimits.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferStatusLimits.to_json())

# convert the object into a dict
admin_archive_transfer_status_limits_dict = admin_archive_transfer_status_limits_instance.to_dict()
# create an instance of AdminArchiveTransferStatusLimits from a dict
admin_archive_transfer_status_limits_from_dict = AdminArchiveTransferStatusLimits.from_dict(admin_archive_transfer_status_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


