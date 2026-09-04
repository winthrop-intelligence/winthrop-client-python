# DeskAdminQueueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**DeskAdminQueueResponseMeta**](DeskAdminQueueResponseMeta.md) |  | 
**data** | [**List[DeskAdminQueueRow]**](DeskAdminQueueRow.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_queue_response import DeskAdminQueueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminQueueResponse from a JSON string
desk_admin_queue_response_instance = DeskAdminQueueResponse.from_json(json)
# print the JSON string representation of the object
print(DeskAdminQueueResponse.to_json())

# convert the object into a dict
desk_admin_queue_response_dict = desk_admin_queue_response_instance.to_dict()
# create an instance of DeskAdminQueueResponse from a dict
desk_admin_queue_response_from_dict = DeskAdminQueueResponse.from_dict(desk_admin_queue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


