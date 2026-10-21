# UpdateAdminAvatarsRequestAvatar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** |  | [optional] 
**image_remote_url** | **str** |  | [optional] 
**crop_x** | **int** |  | [optional] 
**crop_y** | **int** |  | [optional] 
**crop_w** | **int** |  | [optional] 
**crop_h** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_avatars_request_avatar import UpdateAdminAvatarsRequestAvatar

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminAvatarsRequestAvatar from a JSON string
update_admin_avatars_request_avatar_instance = UpdateAdminAvatarsRequestAvatar.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminAvatarsRequestAvatar.to_json())

# convert the object into a dict
update_admin_avatars_request_avatar_dict = update_admin_avatars_request_avatar_instance.to_dict()
# create an instance of UpdateAdminAvatarsRequestAvatar from a dict
update_admin_avatars_request_avatar_from_dict = UpdateAdminAvatarsRequestAvatar.from_dict(update_admin_avatars_request_avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


