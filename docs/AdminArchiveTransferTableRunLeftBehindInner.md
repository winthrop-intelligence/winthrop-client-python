# AdminArchiveTransferTableRunLeftBehindInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | e.g. undated, group_newer, group_referenced, orphaned, skipped_at_copy | 
**count** | **int** |  | 
**sample_ids** | **List[int]** |  | 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_table_run_left_behind_inner import AdminArchiveTransferTableRunLeftBehindInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferTableRunLeftBehindInner from a JSON string
admin_archive_transfer_table_run_left_behind_inner_instance = AdminArchiveTransferTableRunLeftBehindInner.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferTableRunLeftBehindInner.to_json())

# convert the object into a dict
admin_archive_transfer_table_run_left_behind_inner_dict = admin_archive_transfer_table_run_left_behind_inner_instance.to_dict()
# create an instance of AdminArchiveTransferTableRunLeftBehindInner from a dict
admin_archive_transfer_table_run_left_behind_inner_from_dict = AdminArchiveTransferTableRunLeftBehindInner.from_dict(admin_archive_transfer_table_run_left_behind_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


