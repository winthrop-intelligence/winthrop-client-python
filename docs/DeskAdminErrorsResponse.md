# DeskAdminErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[DeskAdminErrorsResponseErrorsInner]**](DeskAdminErrorsResponseErrorsInner.md) | Plain sentences, or DeskFinding objects for a blocked publish | 

## Example

```python
from winthrop_client_python.models.desk_admin_errors_response import DeskAdminErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminErrorsResponse from a JSON string
desk_admin_errors_response_instance = DeskAdminErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(DeskAdminErrorsResponse.to_json())

# convert the object into a dict
desk_admin_errors_response_dict = desk_admin_errors_response_instance.to_dict()
# create an instance of DeskAdminErrorsResponse from a dict
desk_admin_errors_response_from_dict = DeskAdminErrorsResponse.from_dict(desk_admin_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


