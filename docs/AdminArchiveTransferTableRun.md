# AdminArchiveTransferTableRun

The table's latest transfer run; null before the first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**state** | **str** |  | 
**active** | **bool** | Being worked on now (a running request is on this table, or a batch finished in the last 5 minutes). A running run that is not active was interrupted; requesting again continues it. | 
**strategy** | **str** |  | 
**cutoff_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**heartbeat_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**error_message** | **str** |  | [optional] 
**progress_percent** | **float** | How far selection has got through the table&#39;s ids (a guide; ids are not spread evenly) | 
**counts** | [**AdminArchiveTransferTableRunCounts**](AdminArchiveTransferTableRunCounts.md) |  | 
**speed** | [**AdminArchiveTransferTableRunSpeed**](AdminArchiveTransferTableRunSpeed.md) |  | 
**active_seconds** | **int** | Time spent copying, summed over every request that worked on the run; the time between requests is not counted. | 
**left_behind** | [**List[AdminArchiveTransferTableRunLeftBehindInner]**](AdminArchiveTransferTableRunLeftBehindInner.md) |  | 
**conflict_ids** | **List[int]** | Up to 20 ids the archive holds a different version of | 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_table_run import AdminArchiveTransferTableRun

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferTableRun from a JSON string
admin_archive_transfer_table_run_instance = AdminArchiveTransferTableRun.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferTableRun.to_json())

# convert the object into a dict
admin_archive_transfer_table_run_dict = admin_archive_transfer_table_run_instance.to_dict()
# create an instance of AdminArchiveTransferTableRun from a dict
admin_archive_transfer_table_run_from_dict = AdminArchiveTransferTableRun.from_dict(admin_archive_transfer_table_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


