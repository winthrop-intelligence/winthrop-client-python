# DepartmentAdministratorsAdOffice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad** | [**DepartmentAdministratorsAdSeat**](DepartmentAdministratorsAdSeat.md) |  | 
**deputies** | [**List[DepartmentAdministratorStaffRow]**](DepartmentAdministratorStaffRow.md) | Top paid staff after the AD; empty when comp cannot order them | 

## Example

```python
from winthrop_client_python.models.department_administrators_ad_office import DepartmentAdministratorsAdOffice

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAdministratorsAdOffice from a JSON string
department_administrators_ad_office_instance = DepartmentAdministratorsAdOffice.from_json(json)
# print the JSON string representation of the object
print(DepartmentAdministratorsAdOffice.to_json())

# convert the object into a dict
department_administrators_ad_office_dict = department_administrators_ad_office_instance.to_dict()
# create an instance of DepartmentAdministratorsAdOffice from a dict
department_administrators_ad_office_from_dict = DepartmentAdministratorsAdOffice.from_dict(department_administrators_ad_office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


