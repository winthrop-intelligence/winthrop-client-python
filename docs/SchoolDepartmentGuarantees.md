# SchoolDepartmentGuarantees


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**SchoolDepartmentGuaranteesSchool**](SchoolDepartmentGuaranteesSchool.md) |  | 
**conference** | [**SchoolDepartmentOverviewConference**](SchoolDepartmentOverviewConference.md) |  | 
**season_year** | **int** |  | 
**latest_filed_year** | **int** |  | 
**selected_year** | **int** |  | 
**available_years** | **List[int]** |  | 
**quadrant** | [**DepartmentGuaranteesQuadrant**](DepartmentGuaranteesQuadrant.md) |  | 
**filed_line** | [**DepartmentGuaranteesFiledLine**](DepartmentGuaranteesFiledLine.md) |  | 
**committed_out** | [**DepartmentGuaranteesCommittedSide**](DepartmentGuaranteesCommittedSide.md) |  | 
**committed_in** | [**DepartmentGuaranteesCommittedSide**](DepartmentGuaranteesCommittedSide.md) |  | 
**sports** | [**List[DepartmentGuaranteesSportLedger]**](DepartmentGuaranteesSportLedger.md) |  | 
**market** | [**DepartmentGuaranteesMarket**](DepartmentGuaranteesMarket.md) |  | 
**trend** | [**List[DepartmentGuaranteesTrendEntry]**](DepartmentGuaranteesTrendEntry.md) |  | 

## Example

```python
from winthrop_client_python.models.school_department_guarantees import SchoolDepartmentGuarantees

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolDepartmentGuarantees from a JSON string
school_department_guarantees_instance = SchoolDepartmentGuarantees.from_json(json)
# print the JSON string representation of the object
print(SchoolDepartmentGuarantees.to_json())

# convert the object into a dict
school_department_guarantees_dict = school_department_guarantees_instance.to_dict()
# create an instance of SchoolDepartmentGuarantees from a dict
school_department_guarantees_from_dict = SchoolDepartmentGuarantees.from_dict(school_department_guarantees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


