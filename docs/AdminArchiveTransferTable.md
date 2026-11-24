# AdminArchiveTransferTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**run** | [**AdminArchiveTransferTableRun**](AdminArchiveTransferTableRun.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_table import AdminArchiveTransferTable

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferTable from a JSON string
admin_archive_transfer_table_instance = AdminArchiveTransferTable.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferTable.to_json())

# convert the object into a dict
admin_archive_transfer_table_dict = admin_archive_transfer_table_instance.to_dict()
# create an instance of AdminArchiveTransferTable from a dict
admin_archive_transfer_table_from_dict = AdminArchiveTransferTable.from_dict(admin_archive_transfer_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


