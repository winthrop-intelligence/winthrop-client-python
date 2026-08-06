# DepartmentAdministratorsRecentMove


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**kind** | **str** |  | 
**from_school_name** | **str** | For hires, where the person held a seat the season before | 

## Example

```python
from winthrop_client_python.models.department_administrators_recent_move import DepartmentAdministratorsRecentMove

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAdministratorsRecentMove from a JSON string
department_administrators_recent_move_instance = DepartmentAdministratorsRecentMove.from_json(json)
# print the JSON string representation of the object
print(DepartmentAdministratorsRecentMove.to_json())

# convert the object into a dict
department_administrators_recent_move_dict = department_administrators_recent_move_instance.to_dict()
# create an instance of DepartmentAdministratorsRecentMove from a dict
department_administrators_recent_move_from_dict = DepartmentAdministratorsRecentMove.from_dict(department_administrators_recent_move_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


