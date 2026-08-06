# DepartmentAdministrators990Officer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**friendly_id** | **str** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**amount_cents** | **int** |  | 
**fiscal_year** | **int** | The filing year the amount comes from — the disclosed vintage | 

## Example

```python
from winthrop_client_python.models.department_administrators990_officer import DepartmentAdministrators990Officer

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAdministrators990Officer from a JSON string
department_administrators990_officer_instance = DepartmentAdministrators990Officer.from_json(json)
# print the JSON string representation of the object
print(DepartmentAdministrators990Officer.to_json())

# convert the object into a dict
department_administrators990_officer_dict = department_administrators990_officer_instance.to_dict()
# create an instance of DepartmentAdministrators990Officer from a dict
department_administrators990_officer_from_dict = DepartmentAdministrators990Officer.from_dict(department_administrators990_officer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


