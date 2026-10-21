# AdminUserCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**current_position_title** | **str** |  | [optional] 
**current_school_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_user_coach import AdminUserCoach

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserCoach from a JSON string
admin_user_coach_instance = AdminUserCoach.from_json(json)
# print the JSON string representation of the object
print(AdminUserCoach.to_json())

# convert the object into a dict
admin_user_coach_dict = admin_user_coach_instance.to_dict()
# create an instance of AdminUserCoach from a dict
admin_user_coach_from_dict = AdminUserCoach.from_dict(admin_user_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


