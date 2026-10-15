# AdminCoachAvatar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**image_remote_url** | **str** |  | [optional] 
**crop_x** | **float** |  | [optional] 
**crop_y** | **float** |  | [optional] 
**crop_w** | **float** |  | [optional] 
**crop_h** | **float** |  | [optional] 
**small_url** | **str** |  | [optional] 
**medium_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_avatar import AdminCoachAvatar

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachAvatar from a JSON string
admin_coach_avatar_instance = AdminCoachAvatar.from_json(json)
# print the JSON string representation of the object
print(AdminCoachAvatar.to_json())

# convert the object into a dict
admin_coach_avatar_dict = admin_coach_avatar_instance.to_dict()
# create an instance of AdminCoachAvatar from a dict
admin_coach_avatar_from_dict = AdminCoachAvatar.from_dict(admin_coach_avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


