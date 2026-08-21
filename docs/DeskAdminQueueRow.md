# DeskAdminQueueRow

One 06.1 queue row (frontend DeskAdminQueueRow, structured facts only)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The report&#39;s uuid (kind&#x3D;report) or the request&#39;s (kind&#x3D;ask) | 
**kind** | **str** |  | 
**status** | **str** |  | 
**title** | **str** |  | 
**account** | [**DeskAdminAccount**](DeskAdminAccount.md) |  | 
**requested_by** | **str** |  | 
**ask_body** | **str** |  | 
**ask_received_at** | **datetime** |  | 
**due_at** | **datetime** | The under-a-day promise&#39;s edge, pauses added; new asks only | 
**clock_paused** | **bool** |  | 
**has_html** | **bool** |  | 
**artifact_kinds** | **List[str]** |  | 
**published_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**hidden_at** | **datetime** |  | 
**hidden_reason** | **str** |  | 
**open_count** | **int** | Every reader&#39;s opens, summed | 
**activity_at** | **datetime** | The row&#39;s sort key (newest first) | 

## Example

```python
from winthrop_client_python.models.desk_admin_queue_row import DeskAdminQueueRow

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminQueueRow from a JSON string
desk_admin_queue_row_instance = DeskAdminQueueRow.from_json(json)
# print the JSON string representation of the object
print(DeskAdminQueueRow.to_json())

# convert the object into a dict
desk_admin_queue_row_dict = desk_admin_queue_row_instance.to_dict()
# create an instance of DeskAdminQueueRow from a dict
desk_admin_queue_row_from_dict = DeskAdminQueueRow.from_dict(desk_admin_queue_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


