# DepartmentCoachSeatCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**interim** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.department_coach_seat_coach import DepartmentCoachSeatCoach

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachSeatCoach from a JSON string
department_coach_seat_coach_instance = DepartmentCoachSeatCoach.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachSeatCoach.to_json())

# convert the object into a dict
department_coach_seat_coach_dict = department_coach_seat_coach_instance.to_dict()
# create an instance of DepartmentCoachSeatCoach from a dict
department_coach_seat_coach_from_dict = DepartmentCoachSeatCoach.from_dict(department_coach_seat_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


