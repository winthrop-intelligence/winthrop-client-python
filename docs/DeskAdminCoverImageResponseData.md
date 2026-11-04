# DeskAdminCoverImageResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot** | **str** |  | 
**image** | [**DeskAdminCoverImage**](DeskAdminCoverImage.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_cover_image_response_data import DeskAdminCoverImageResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminCoverImageResponseData from a JSON string
desk_admin_cover_image_response_data_instance = DeskAdminCoverImageResponseData.from_json(json)
# print the JSON string representation of the object
print(DeskAdminCoverImageResponseData.to_json())

# convert the object into a dict
desk_admin_cover_image_response_data_dict = desk_admin_cover_image_response_data_instance.to_dict()
# create an instance of DeskAdminCoverImageResponseData from a dict
desk_admin_cover_image_response_data_from_dict = DeskAdminCoverImageResponseData.from_dict(desk_admin_cover_image_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


