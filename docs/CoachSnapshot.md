# CoachSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year_str** | **str** |  | 
**base_comp_cents** | **int** |  | [optional] 
**total_comp_cents** | **int** |  | [optional] 
**compensation_type** | **str** |  | 
**buyout_terms** | **str** |  | [optional] 
**record** | **str** |  | [optional] 
**contract_start** | **str** |  | [optional] 
**contract_end** | **str** |  | [optional] 
**contract_at_will** | **bool** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**income_reports** | [**List[SnapshotIncomeReport]**](SnapshotIncomeReport.md) |  | [optional] 
**asst_coach_pool_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_snapshot import CoachSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of CoachSnapshot from a JSON string
coach_snapshot_instance = CoachSnapshot.from_json(json)
# print the JSON string representation of the object
print(CoachSnapshot.to_json())

# convert the object into a dict
coach_snapshot_dict = coach_snapshot_instance.to_dict()
# create an instance of CoachSnapshot from a dict
coach_snapshot_from_dict = CoachSnapshot.from_dict(coach_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


