# DeskAdminPublishResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeskAdminPublishResponseData**](DeskAdminPublishResponseData.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_publish_response import DeskAdminPublishResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminPublishResponse from a JSON string
desk_admin_publish_response_instance = DeskAdminPublishResponse.from_json(json)
# print the JSON string representation of the object
print(DeskAdminPublishResponse.to_json())

# convert the object into a dict
desk_admin_publish_response_dict = desk_admin_publish_response_instance.to_dict()
# create an instance of DeskAdminPublishResponse from a dict
desk_admin_publish_response_from_dict = DeskAdminPublishResponse.from_dict(desk_admin_publish_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


