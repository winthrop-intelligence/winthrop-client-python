# SchoolDepartmentAdministrators


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**SchoolDepartmentGuaranteesSchool**](SchoolDepartmentGuaranteesSchool.md) |  | 
**conference** | [**SchoolDepartmentOverviewConference**](SchoolDepartmentOverviewConference.md) |  | 
**mode** | **str** |  | 
**selected_year** | **int** |  | 
**available_years** | **List[int]** |  | 
**comp_visible** | **bool** |  | 
**staff_count** | **int** |  | 
**staff** | [**List[DepartmentAdministratorStaffRow]**](DepartmentAdministratorStaffRow.md) |  | 
**staff_stats** | [**DepartmentAdministratorsStaffStats**](DepartmentAdministratorsStaffStats.md) |  | 
**ad_office** | [**DepartmentAdministratorsAdOffice**](DepartmentAdministratorsAdOffice.md) |  | 
**recent_moves** | [**List[DepartmentAdministratorsRecentMove]**](DepartmentAdministratorsRecentMove.md) |  | 
**scorecard** | [**DepartmentAdministratorsScorecard**](DepartmentAdministratorsScorecard.md) |  | 
**scorecard_gap** | [**DepartmentAdministratorsScorecardGap**](DepartmentAdministratorsScorecardGap.md) |  | 
**officers_990** | [**List[DepartmentAdministrators990Officer]**](DepartmentAdministrators990Officer.md) |  | 
**ad_profile** | [**DepartmentAdministratorsAdProfile**](DepartmentAdministratorsAdProfile.md) |  | 
**basis** | [**DepartmentAdministratorsBasis**](DepartmentAdministratorsBasis.md) |  | 

## Example

```python
from winthrop_client_python.models.school_department_administrators import SchoolDepartmentAdministrators

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolDepartmentAdministrators from a JSON string
school_department_administrators_instance = SchoolDepartmentAdministrators.from_json(json)
# print the JSON string representation of the object
print(SchoolDepartmentAdministrators.to_json())

# convert the object into a dict
school_department_administrators_dict = school_department_administrators_instance.to_dict()
# create an instance of SchoolDepartmentAdministrators from a dict
school_department_administrators_from_dict = SchoolDepartmentAdministrators.from_dict(school_department_administrators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


