# AdminArchiveTransferTableRunCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_rows** | **int** |  | [optional] 
**copied_rows** | **int** |  | [optional] 
**already_present_rows** | **int** |  | [optional] 
**verified_rows** | **int** |  | [optional] 
**skipped_rows** | **int** |  | [optional] 
**conflicted_rows** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_table_run_counts import AdminArchiveTransferTableRunCounts

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferTableRunCounts from a JSON string
admin_archive_transfer_table_run_counts_instance = AdminArchiveTransferTableRunCounts.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferTableRunCounts.to_json())

# convert the object into a dict
admin_archive_transfer_table_run_counts_dict = admin_archive_transfer_table_run_counts_instance.to_dict()
# create an instance of AdminArchiveTransferTableRunCounts from a dict
admin_archive_transfer_table_run_counts_from_dict = AdminArchiveTransferTableRunCounts.from_dict(admin_archive_transfer_table_run_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


