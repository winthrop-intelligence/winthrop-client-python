# DepartmentOverviewProvenance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filing_year** | **int** |  | 
**cohort_size** | **int** |  | 
**reporting_count** | **int** |  | 
**non_reporting** | [**List[DepartmentOverviewNonReportingSchool]**](DepartmentOverviewNonReportingSchool.md) |  | 

## Example

```python
from winthrop_client_python.models.department_overview_provenance import DepartmentOverviewProvenance

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewProvenance from a JSON string
department_overview_provenance_instance = DepartmentOverviewProvenance.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewProvenance.to_json())

# convert the object into a dict
department_overview_provenance_dict = department_overview_provenance_instance.to_dict()
# create an instance of DepartmentOverviewProvenance from a dict
department_overview_provenance_from_dict = DepartmentOverviewProvenance.from_dict(department_overview_provenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


