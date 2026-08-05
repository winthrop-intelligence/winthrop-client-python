# DepartmentOverviewHeadlineStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**label** | **str** |  | 
**amount_cents** | **int** |  | 
**rank** | **int** |  | 
**cohort_size** | **int** |  | 
**partial_cohort** | **bool** |  | 
**neighbour** | [**DepartmentOverviewNeighbour**](DepartmentOverviewNeighbour.md) |  | 

## Example

```python
from winthrop_client_python.models.department_overview_headline_stat import DepartmentOverviewHeadlineStat

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewHeadlineStat from a JSON string
department_overview_headline_stat_instance = DepartmentOverviewHeadlineStat.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewHeadlineStat.to_json())

# convert the object into a dict
department_overview_headline_stat_dict = department_overview_headline_stat_instance.to_dict()
# create an instance of DepartmentOverviewHeadlineStat from a dict
department_overview_headline_stat_from_dict = DepartmentOverviewHeadlineStat.from_dict(department_overview_headline_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


