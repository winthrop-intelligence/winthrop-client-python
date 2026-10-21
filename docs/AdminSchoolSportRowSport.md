# AdminSchoolSportRowSport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**gender_code** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_sport_row_sport import AdminSchoolSportRowSport

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolSportRowSport from a JSON string
admin_school_sport_row_sport_instance = AdminSchoolSportRowSport.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolSportRowSport.to_json())

# convert the object into a dict
admin_school_sport_row_sport_dict = admin_school_sport_row_sport_instance.to_dict()
# create an instance of AdminSchoolSportRowSport from a dict
admin_school_sport_row_sport_from_dict = AdminSchoolSportRowSport.from_dict(admin_school_sport_row_sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


