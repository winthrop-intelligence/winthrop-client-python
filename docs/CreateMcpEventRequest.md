# CreateMcpEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mcp_event** | [**CreateMcpEventRequestMcpEvent**](CreateMcpEventRequestMcpEvent.md) |  | 

## Example

```python
from winthrop_client_python.models.create_mcp_event_request import CreateMcpEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMcpEventRequest from a JSON string
create_mcp_event_request_instance = CreateMcpEventRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMcpEventRequest.to_json())

# convert the object into a dict
create_mcp_event_request_dict = create_mcp_event_request_instance.to_dict()
# create an instance of CreateMcpEventRequest from a dict
create_mcp_event_request_from_dict = CreateMcpEventRequest.from_dict(create_mcp_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


