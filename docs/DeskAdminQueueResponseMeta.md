# DeskAdminQueueResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** |  | 
**counts** | **Dict[str, int]** |  | 
**accounts** | [**List[DeskAdminAccount]**](DeskAdminAccount.md) |  | 
**every_school_user_count** | **int** | How many people an every-school publish reaches right now — the compose screen&#39;s confirm (WINAD-10415 / D-29).  | 

## Example

```python
from winthrop_client_python.models.desk_admin_queue_response_meta import DeskAdminQueueResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminQueueResponseMeta from a JSON string
desk_admin_queue_response_meta_instance = DeskAdminQueueResponseMeta.from_json(json)
# print the JSON string representation of the object
print(DeskAdminQueueResponseMeta.to_json())

# convert the object into a dict
desk_admin_queue_response_meta_dict = desk_admin_queue_response_meta_instance.to_dict()
# create an instance of DeskAdminQueueResponseMeta from a dict
desk_admin_queue_response_meta_from_dict = DeskAdminQueueResponseMeta.from_dict(desk_admin_queue_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


