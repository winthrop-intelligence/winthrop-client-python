# CreateMcpEventRequestMcpEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_uuid** | **str** | Client-generated unique identifier used for idempotency | 
**event_name** | **str** | Name of the event (e.g. \&quot;mcp.tool.called\&quot;) | 
**tool_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**workflow_id** | **str** |  | [optional] 
**rationale** | **str** |  | [optional] 
**intent** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**duration_ms** | **int** |  | [optional] 
**error_class** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**object_refs** | **Dict[str, object]** |  | [optional] 
**artifact_refs** | **Dict[str, object]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_mcp_event_request_mcp_event import CreateMcpEventRequestMcpEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMcpEventRequestMcpEvent from a JSON string
create_mcp_event_request_mcp_event_instance = CreateMcpEventRequestMcpEvent.from_json(json)
# print the JSON string representation of the object
print(CreateMcpEventRequestMcpEvent.to_json())

# convert the object into a dict
create_mcp_event_request_mcp_event_dict = create_mcp_event_request_mcp_event_instance.to_dict()
# create an instance of CreateMcpEventRequestMcpEvent from a dict
create_mcp_event_request_mcp_event_from_dict = CreateMcpEventRequestMcpEvent.from_dict(create_mcp_event_request_mcp_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


