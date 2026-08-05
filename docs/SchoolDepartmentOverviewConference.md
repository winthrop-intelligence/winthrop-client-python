# SchoolDepartmentOverviewConference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.school_department_overview_conference import SchoolDepartmentOverviewConference

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolDepartmentOverviewConference from a JSON string
school_department_overview_conference_instance = SchoolDepartmentOverviewConference.from_json(json)
# print the JSON string representation of the object
print(SchoolDepartmentOverviewConference.to_json())

# convert the object into a dict
school_department_overview_conference_dict = school_department_overview_conference_instance.to_dict()
# create an instance of SchoolDepartmentOverviewConference from a dict
school_department_overview_conference_from_dict = SchoolDepartmentOverviewConference.from_dict(school_department_overview_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


