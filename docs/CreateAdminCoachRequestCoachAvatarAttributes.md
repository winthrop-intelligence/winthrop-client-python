# CreateAdminCoachRequestCoachAvatarAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**image** | **bytearray** |  | [optional] 
**image_remote_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_coach_request_coach_avatar_attributes import CreateAdminCoachRequestCoachAvatarAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminCoachRequestCoachAvatarAttributes from a JSON string
create_admin_coach_request_coach_avatar_attributes_instance = CreateAdminCoachRequestCoachAvatarAttributes.from_json(json)
# print the JSON string representation of the object
print(CreateAdminCoachRequestCoachAvatarAttributes.to_json())

# convert the object into a dict
create_admin_coach_request_coach_avatar_attributes_dict = create_admin_coach_request_coach_avatar_attributes_instance.to_dict()
# create an instance of CreateAdminCoachRequestCoachAvatarAttributes from a dict
create_admin_coach_request_coach_avatar_attributes_from_dict = CreateAdminCoachRequestCoachAvatarAttributes.from_dict(create_admin_coach_request_coach_avatar_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


