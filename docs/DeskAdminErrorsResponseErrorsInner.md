# DeskAdminErrorsResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**severity** | **str** |  | 
**message** | **str** |  | 
**line** | **int** |  | 
**node_hint** | **str** |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_errors_response_errors_inner import DeskAdminErrorsResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminErrorsResponseErrorsInner from a JSON string
desk_admin_errors_response_errors_inner_instance = DeskAdminErrorsResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(DeskAdminErrorsResponseErrorsInner.to_json())

# convert the object into a dict
desk_admin_errors_response_errors_inner_dict = desk_admin_errors_response_errors_inner_instance.to_dict()
# create an instance of DeskAdminErrorsResponseErrorsInner from a dict
desk_admin_errors_response_errors_inner_from_dict = DeskAdminErrorsResponseErrorsInner.from_dict(desk_admin_errors_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


