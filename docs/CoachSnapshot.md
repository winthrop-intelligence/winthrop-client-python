# CoachSnapshot

Compensation resolves for the selected assignment in the system's current season, carrying forward at most two seasons within the same continuous job. History stays as reported. The snapshot is null without compensation access or a selected position. season_year_str, performance, income reports and current contract fields retain their assignment context; compensation_source_year identifies the salary's actual season. Hourly current records retain their stored values and type; no annualization occurs. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year_str** | **str** |  | 
**base_comp_cents** | **int** | Base from the resolved compensation record, in cents; null when unavailable. | 
**total_comp_cents** | **int** | Guaranteed total from the same resolved record, in cents; null when unavailable. | 
**compensation_type** | **str** | Resolved record&#39;s type, or null when compensation is unavailable. | 
**compensation_source_year** | **int** | Salary source season end year; null when unavailable, never inferred from contract dates. | 
**compensation_is_fallback** | **bool** | True only when salary comes from an earlier eligible season; false when unavailable. | 
**compensation_source_compensation_id** | **int** | Resolved compensation id; null when unavailable. Gated with amounts by compensation access. | 
**compensation_source_raw_contract_id** | **int** | Salary source document id; omitted unless both its contract and document are authorized. | [optional] 
**buyout_terms** | **str** |  | 
**record** | **str** |  | [optional] 
**contract_start** | **str** |  | [optional] 
**contract_end** | **str** |  | [optional] 
**contract_at_will** | **bool** |  | [optional] 
**raw_contract_id** | **int** | Selected position&#39;s current contract document, never replaced by the salary source document. | [optional] 
**income_reports** | [**List[SnapshotIncomeReport]**](SnapshotIncomeReport.md) |  | [optional] 
**asst_coach_pool_cents** | **int** |  | 

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


