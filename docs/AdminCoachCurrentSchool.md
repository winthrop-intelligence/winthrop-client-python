# AdminCoachCurrentSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name_or_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_current_school import AdminCoachCurrentSchool

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachCurrentSchool from a JSON string
admin_coach_current_school_instance = AdminCoachCurrentSchool.from_json(json)
# print the JSON string representation of the object
print(AdminCoachCurrentSchool.to_json())

# convert the object into a dict
admin_coach_current_school_dict = admin_coach_current_school_instance.to_dict()
# create an instance of AdminCoachCurrentSchool from a dict
admin_coach_current_school_from_dict = AdminCoachCurrentSchool.from_dict(admin_coach_current_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


