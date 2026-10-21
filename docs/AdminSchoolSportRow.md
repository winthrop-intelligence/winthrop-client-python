# AdminSchoolSportRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport** | [**AdminSchoolSportRowSport**](AdminSchoolSportRowSport.md) |  | [optional] 
**conference** | [**AdminCoachHometownState**](AdminCoachHometownState.md) |  | [optional] 
**conferenceship_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_sport_row import AdminSchoolSportRow

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolSportRow from a JSON string
admin_school_sport_row_instance = AdminSchoolSportRow.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolSportRow.to_json())

# convert the object into a dict
admin_school_sport_row_dict = admin_school_sport_row_instance.to_dict()
# create an instance of AdminSchoolSportRow from a dict
admin_school_sport_row_from_dict = AdminSchoolSportRow.from_dict(admin_school_sport_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


