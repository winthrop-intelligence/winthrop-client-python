# DepartmentOverviewNeighbour


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**name** | **str** |  | 
**amount_cents** | **int** |  | 
**direction** | **str** | \&quot;above\&quot; when the peer outspends the subject, \&quot;next\&quot; when the subject leads | 
**delta_cents** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_overview_neighbour import DepartmentOverviewNeighbour

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewNeighbour from a JSON string
department_overview_neighbour_instance = DepartmentOverviewNeighbour.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewNeighbour.to_json())

# convert the object into a dict
department_overview_neighbour_dict = department_overview_neighbour_instance.to_dict()
# create an instance of DepartmentOverviewNeighbour from a dict
department_overview_neighbour_from_dict = DepartmentOverviewNeighbour.from_dict(department_overview_neighbour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


