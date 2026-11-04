# DeskAdminCoverImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeskAdminCoverImageResponseData**](DeskAdminCoverImageResponseData.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_cover_image_response import DeskAdminCoverImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminCoverImageResponse from a JSON string
desk_admin_cover_image_response_instance = DeskAdminCoverImageResponse.from_json(json)
# print the JSON string representation of the object
print(DeskAdminCoverImageResponse.to_json())

# convert the object into a dict
desk_admin_cover_image_response_dict = desk_admin_cover_image_response_instance.to_dict()
# create an instance of DeskAdminCoverImageResponse from a dict
desk_admin_cover_image_response_from_dict = DeskAdminCoverImageResponse.from_dict(desk_admin_cover_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


