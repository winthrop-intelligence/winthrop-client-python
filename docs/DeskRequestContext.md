# DeskRequestContext

Provenance of a report built from an ask (04.2 first-open strip)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uuid** | **str** |  | 
**requester_name** | **str** |  | 
**requested_at** | **datetime** |  | 
**quote** | **str** | The ask&#39;s body | 
**delivered_in_label** | **str** | Backend-committed copy (\&quot;delivered in 2 days\&quot;) | 

## Example

```python
from winthrop_client_python.models.desk_request_context import DeskRequestContext

# TODO update the JSON string below
json = "{}"
# create an instance of DeskRequestContext from a JSON string
desk_request_context_instance = DeskRequestContext.from_json(json)
# print the JSON string representation of the object
print(DeskRequestContext.to_json())

# convert the object into a dict
desk_request_context_dict = desk_request_context_instance.to_dict()
# create an instance of DeskRequestContext from a dict
desk_request_context_from_dict = DeskRequestContext.from_dict(desk_request_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


