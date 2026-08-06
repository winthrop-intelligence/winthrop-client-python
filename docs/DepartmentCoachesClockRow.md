# DepartmentCoachesClockRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_abbrev** | **str** |  | 
**group** | **str** |  | 
**names** | **List[str]** |  | 
**state** | **str** |  | 
**var_date** | **str** |  | 
**approximate** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.department_coaches_clock_row import DepartmentCoachesClockRow

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachesClockRow from a JSON string
department_coaches_clock_row_instance = DepartmentCoachesClockRow.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachesClockRow.to_json())

# convert the object into a dict
department_coaches_clock_row_dict = department_coaches_clock_row_instance.to_dict()
# create an instance of DepartmentCoachesClockRow from a dict
department_coaches_clock_row_from_dict = DepartmentCoachesClockRow.from_dict(department_coaches_clock_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


