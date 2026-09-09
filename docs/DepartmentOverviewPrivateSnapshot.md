# DepartmentOverviewPrivateSnapshot

The department's shape in the EADA figures its filing breaks out (WINAD-10390) — total expenses and revenue, plus the two sports the filing breaks out — from the same ledger the Financials tab reads. Four lines at most, and about half of filers state fewer: the ledger keeps only what the filing reports a positive figure for, so a department that sponsors no football has no football line. Null when no EADA report is on file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**lines** | [**List[DepartmentOverviewPrivateSnapshotLine]**](DepartmentOverviewPrivateSnapshotLine.md) |  | 

## Example

```python
from winthrop_client_python.models.department_overview_private_snapshot import DepartmentOverviewPrivateSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateSnapshot from a JSON string
department_overview_private_snapshot_instance = DepartmentOverviewPrivateSnapshot.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateSnapshot.to_json())

# convert the object into a dict
department_overview_private_snapshot_dict = department_overview_private_snapshot_instance.to_dict()
# create an instance of DepartmentOverviewPrivateSnapshot from a dict
department_overview_private_snapshot_from_dict = DepartmentOverviewPrivateSnapshot.from_dict(department_overview_private_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


