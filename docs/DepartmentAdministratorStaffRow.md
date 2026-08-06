# DepartmentAdministratorStaffRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**friendly_id** | **str** |  | 
**name** | **str** |  | 
**last_name** | **str** | Canonical surname from the roster record — display labels must not re-parse the full name | 
**title** | **str** |  | 
**departments** | **List[str]** |  | 
**is_ad** | **bool** |  | 
**comp_cents** | **int** | Null in private mode and for viewers without the administrator_compensation ability | 
**comp_basis** | **str** |  | 
**comp_estimated** | **bool** | True when the amount is a 990 filing rather than a salary record — the asterisk | 

## Example

```python
from winthrop_client_python.models.department_administrator_staff_row import DepartmentAdministratorStaffRow

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAdministratorStaffRow from a JSON string
department_administrator_staff_row_instance = DepartmentAdministratorStaffRow.from_json(json)
# print the JSON string representation of the object
print(DepartmentAdministratorStaffRow.to_json())

# convert the object into a dict
department_administrator_staff_row_dict = department_administrator_staff_row_instance.to_dict()
# create an instance of DepartmentAdministratorStaffRow from a dict
department_administrator_staff_row_from_dict = DepartmentAdministratorStaffRow.from_dict(department_administrator_staff_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


