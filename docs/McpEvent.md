# McpEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**event_uuid** | **str** |  | 
**event_name** | **str** |  | 
**user_id** | **int** |  | 
**account_id** | **int** |  | 
**school_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.mcp_event import McpEvent

# TODO update the JSON string below
json = "{}"
# create an instance of McpEvent from a JSON string
mcp_event_instance = McpEvent.from_json(json)
# print the JSON string representation of the object
print(McpEvent.to_json())

# convert the object into a dict
mcp_event_dict = mcp_event_instance.to_dict()
# create an instance of McpEvent from a dict
mcp_event_from_dict = McpEvent.from_dict(mcp_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


