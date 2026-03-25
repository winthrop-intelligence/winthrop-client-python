# SnapshotIncomeReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**year** | **int** |  | 
**raw_contract_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.snapshot_income_report import SnapshotIncomeReport

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotIncomeReport from a JSON string
snapshot_income_report_instance = SnapshotIncomeReport.from_json(json)
# print the JSON string representation of the object
print(SnapshotIncomeReport.to_json())

# convert the object into a dict
snapshot_income_report_dict = snapshot_income_report_instance.to_dict()
# create an instance of SnapshotIncomeReport from a dict
snapshot_income_report_from_dict = SnapshotIncomeReport.from_dict(snapshot_income_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


