# SchoolDepartmentCoaches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**SchoolDepartmentGuaranteesSchool**](SchoolDepartmentGuaranteesSchool.md) |  | 
**conference** | [**SchoolDepartmentOverviewConference**](SchoolDepartmentOverviewConference.md) |  | 
**mode** | **str** |  | 
**selected_year** | **int** |  | 
**available_years** | **List[int]** |  | 
**seat_count** | **int** |  | 
**result_window** | [**DepartmentCoachesResultWindow**](DepartmentCoachesResultWindow.md) |  | 
**seats** | [**List[DepartmentCoachSeat]**](DepartmentCoachSeat.md) |  | 
**quadrant** | [**DepartmentCoachesQuadrant**](DepartmentCoachesQuadrant.md) |  | 
**portfolio_shape** | [**DepartmentCoachesPortfolioShape**](DepartmentCoachesPortfolioShape.md) |  | 
**contract_clocks** | [**DepartmentCoachesContractClocks**](DepartmentCoachesContractClocks.md) |  | 
**basis** | [**DepartmentCoachesBasis**](DepartmentCoachesBasis.md) |  | 

## Example

```python
from winthrop_client_python.models.school_department_coaches import SchoolDepartmentCoaches

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolDepartmentCoaches from a JSON string
school_department_coaches_instance = SchoolDepartmentCoaches.from_json(json)
# print the JSON string representation of the object
print(SchoolDepartmentCoaches.to_json())

# convert the object into a dict
school_department_coaches_dict = school_department_coaches_instance.to_dict()
# create an instance of SchoolDepartmentCoaches from a dict
school_department_coaches_from_dict = SchoolDepartmentCoaches.from_dict(school_department_coaches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


