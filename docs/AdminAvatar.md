# AdminAvatar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**image_remote_url** | **str** |  | [optional] 
**crop_x** | **int** |  | [optional] 
**crop_y** | **int** |  | [optional] 
**crop_w** | **int** |  | [optional] 
**crop_h** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**small_url** | **str** |  | [optional] 
**medium_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_avatar import AdminAvatar

# TODO update the JSON string below
json = "{}"
# create an instance of AdminAvatar from a JSON string
admin_avatar_instance = AdminAvatar.from_json(json)
# print the JSON string representation of the object
print(AdminAvatar.to_json())

# convert the object into a dict
admin_avatar_dict = admin_avatar_instance.to_dict()
# create an instance of AdminAvatar from a dict
admin_avatar_from_dict = AdminAvatar.from_dict(admin_avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


