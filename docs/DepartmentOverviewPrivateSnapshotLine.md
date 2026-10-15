# DepartmentOverviewPrivateSnapshotLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**label** | **str** |  | 
**amount_cents** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_overview_private_snapshot_line import DepartmentOverviewPrivateSnapshotLine

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateSnapshotLine from a JSON string
department_overview_private_snapshot_line_instance = DepartmentOverviewPrivateSnapshotLine.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateSnapshotLine.to_json())

# convert the object into a dict
department_overview_private_snapshot_line_dict = department_overview_private_snapshot_line_instance.to_dict()
# create an instance of DepartmentOverviewPrivateSnapshotLine from a dict
department_overview_private_snapshot_line_from_dict = DepartmentOverviewPrivateSnapshotLine.from_dict(department_overview_private_snapshot_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


