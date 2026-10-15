# AdminCoachCurrentSport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_current_sport import AdminCoachCurrentSport

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachCurrentSport from a JSON string
admin_coach_current_sport_instance = AdminCoachCurrentSport.from_json(json)
# print the JSON string representation of the object
print(AdminCoachCurrentSport.to_json())

# convert the object into a dict
admin_coach_current_sport_dict = admin_coach_current_sport_instance.to_dict()
# create an instance of AdminCoachCurrentSport from a dict
admin_coach_current_sport_from_dict = AdminCoachCurrentSport.from_dict(admin_coach_current_sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


