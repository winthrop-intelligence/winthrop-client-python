# DeskRequest

A pending ask (frontend DeskRequest)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**body** | **str** |  | 
**title** | **str** | Working title for the pending card (context.working_title) | 
**category** | **str** |  | 
**status** | **str** |  | 
**requester_name** | **str** |  | 
**requested_by_viewer** | **bool** |  | 
**requested_at** | **datetime** |  | 
**delivers_label** | **str** |  | 
**source_report_uuid** | **str** |  | 
**cta_key** | **str** |  | 
**client_note** | **str** | The needs-more-info note shown on the customer&#39;s pending card. Was &#x60;admin_note&#x60;, which read as internal-only while being rendered to the customer — a naming trap on a live field. The old key still ships alongside this one until the generated client is regenerated from this spec; drop it then.  | 
**admin_note** | **str** | Deprecated alias for client_note. Remove once clients are regenerated. | [optional] 

## Example

```python
from winthrop_client_python.models.desk_request import DeskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeskRequest from a JSON string
desk_request_instance = DeskRequest.from_json(json)
# print the JSON string representation of the object
print(DeskRequest.to_json())

# convert the object into a dict
desk_request_dict = desk_request_instance.to_dict()
# create an instance of DeskRequest from a dict
desk_request_from_dict = DeskRequest.from_dict(desk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


