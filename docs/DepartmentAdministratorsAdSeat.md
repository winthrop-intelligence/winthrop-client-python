# DepartmentAdministratorsAdSeat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**friendly_id** | **str** |  | 
**name** | **str** |  | 
**last_name** | **str** |  | 
**title** | **str** |  | 
**departments** | **List[str]** |  | 
**is_ad** | **bool** |  | 
**comp_cents** | **int** |  | 
**comp_basis** | **str** |  | 
**comp_estimated** | **bool** |  | 
**tenure_years** | **int** | Seasons since first holding the AD position type at this school, inclusive | 
**comp_year** | **int** | The compensation record&#39;s own year — the vintage label for 990 amounts | 

## Example

```python
from winthrop_client_python.models.department_administrators_ad_seat import DepartmentAdministratorsAdSeat

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAdministratorsAdSeat from a JSON string
department_administrators_ad_seat_instance = DepartmentAdministratorsAdSeat.from_json(json)
# print the JSON string representation of the object
print(DepartmentAdministratorsAdSeat.to_json())

# convert the object into a dict
department_administrators_ad_seat_dict = department_administrators_ad_seat_instance.to_dict()
# create an instance of DepartmentAdministratorsAdSeat from a dict
department_administrators_ad_seat_from_dict = DepartmentAdministratorsAdSeat.from_dict(department_administrators_ad_seat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


