# CreatePageViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route** | **str** | The frontend route (pathname) being viewed | 
**search** | **str** | The query string for the viewed route, including the leading \&quot;?\&quot; | [optional] 
**tab** | **str** | Client-derived feature area for the route (e.g. coach, gad, rad, deals). Server validates against an allowlist and falls back to \&quot;other\&quot;. | [optional] 

## Example

```python
from winthrop_client_python.models.create_page_view_request import CreatePageViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePageViewRequest from a JSON string
create_page_view_request_instance = CreatePageViewRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePageViewRequest.to_json())

# convert the object into a dict
create_page_view_request_dict = create_page_view_request_instance.to_dict()
# create an instance of CreatePageViewRequest from a dict
create_page_view_request_from_dict = CreatePageViewRequest.from_dict(create_page_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


