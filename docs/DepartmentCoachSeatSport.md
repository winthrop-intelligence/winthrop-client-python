# DepartmentCoachSeatSport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**key** | **str** |  | 
**name** | **str** |  | 
**abbrev** | **str** |  | 

## Example

```python
from winthrop_client_python.models.department_coach_seat_sport import DepartmentCoachSeatSport

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachSeatSport from a JSON string
department_coach_seat_sport_instance = DepartmentCoachSeatSport.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachSeatSport.to_json())

# convert the object into a dict
department_coach_seat_sport_dict = department_coach_seat_sport_instance.to_dict()
# create an instance of DepartmentCoachSeatSport from a dict
department_coach_seat_sport_from_dict = DepartmentCoachSeatSport.from_dict(department_coach_seat_sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


