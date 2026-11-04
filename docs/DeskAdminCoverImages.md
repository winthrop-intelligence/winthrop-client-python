# DeskAdminCoverImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**DeskAdminCoverImage**](DeskAdminCoverImage.md) |  | 
**banner** | [**DeskAdminCoverImage**](DeskAdminCoverImage.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_cover_images import DeskAdminCoverImages

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminCoverImages from a JSON string
desk_admin_cover_images_instance = DeskAdminCoverImages.from_json(json)
# print the JSON string representation of the object
print(DeskAdminCoverImages.to_json())

# convert the object into a dict
desk_admin_cover_images_dict = desk_admin_cover_images_instance.to_dict()
# create an instance of DeskAdminCoverImages from a dict
desk_admin_cover_images_from_dict = DeskAdminCoverImages.from_dict(desk_admin_cover_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


