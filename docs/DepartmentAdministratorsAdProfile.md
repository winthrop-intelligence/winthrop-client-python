# DepartmentAdministratorsAdProfile

Private-mode AD card — roster facts only, no money

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**friendly_id** | **str** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**in_seat_since** | **date** | Filed contract start date when one exists | 
**since_year** | **int** | First season holding the AD position type at this school | 
**years_at_school** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_administrators_ad_profile import DepartmentAdministratorsAdProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAdministratorsAdProfile from a JSON string
department_administrators_ad_profile_instance = DepartmentAdministratorsAdProfile.from_json(json)
# print the JSON string representation of the object
print(DepartmentAdministratorsAdProfile.to_json())

# convert the object into a dict
department_administrators_ad_profile_dict = department_administrators_ad_profile_instance.to_dict()
# create an instance of DepartmentAdministratorsAdProfile from a dict
department_administrators_ad_profile_from_dict = DepartmentAdministratorsAdProfile.from_dict(department_administrators_ad_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


