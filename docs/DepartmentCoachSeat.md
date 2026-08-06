# DepartmentCoachSeat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport** | [**DepartmentCoachSeatSport**](DepartmentCoachSeatSport.md) |  | 
**coach** | [**DepartmentCoachSeatCoach**](DepartmentCoachSeatCoach.md) |  | 
**pay** | [**DepartmentCoachPay**](DepartmentCoachPay.md) |  | 
**result** | [**DepartmentCoachResult**](DepartmentCoachResult.md) |  | 
**verdict** | [**DepartmentCoachVerdict**](DepartmentCoachVerdict.md) |  | 
**quadrant_point** | [**DepartmentCoachQuadrantPoint**](DepartmentCoachQuadrantPoint.md) |  | 
**unplotted_reason** | **str** |  | 

## Example

```python
from winthrop_client_python.models.department_coach_seat import DepartmentCoachSeat

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachSeat from a JSON string
department_coach_seat_instance = DepartmentCoachSeat.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachSeat.to_json())

# convert the object into a dict
department_coach_seat_dict = department_coach_seat_instance.to_dict()
# create an instance of DepartmentCoachSeat from a dict
department_coach_seat_from_dict = DepartmentCoachSeat.from_dict(department_coach_seat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


