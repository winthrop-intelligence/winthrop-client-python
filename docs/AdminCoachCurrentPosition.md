# AdminCoachCurrentPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**departing** | **bool** |  | [optional] 
**position_type_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_current_position import AdminCoachCurrentPosition

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachCurrentPosition from a JSON string
admin_coach_current_position_instance = AdminCoachCurrentPosition.from_json(json)
# print the JSON string representation of the object
print(AdminCoachCurrentPosition.to_json())

# convert the object into a dict
admin_coach_current_position_dict = admin_coach_current_position_instance.to_dict()
# create an instance of AdminCoachCurrentPosition from a dict
admin_coach_current_position_from_dict = AdminCoachCurrentPosition.from_dict(admin_coach_current_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


