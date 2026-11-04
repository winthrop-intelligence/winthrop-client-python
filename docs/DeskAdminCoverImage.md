# DeskAdminCoverImage

One stored cover image (WINAD-10725); null when the slot is empty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**byte_size** | **int** |  | 
**url** | **str** | Expiring Active Storage link; fetch with the bearer token. | 

## Example

```python
from winthrop_client_python.models.desk_admin_cover_image import DeskAdminCoverImage

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminCoverImage from a JSON string
desk_admin_cover_image_instance = DeskAdminCoverImage.from_json(json)
# print the JSON string representation of the object
print(DeskAdminCoverImage.to_json())

# convert the object into a dict
desk_admin_cover_image_dict = desk_admin_cover_image_instance.to_dict()
# create an instance of DeskAdminCoverImage from a dict
desk_admin_cover_image_from_dict = DeskAdminCoverImage.from_dict(desk_admin_cover_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


