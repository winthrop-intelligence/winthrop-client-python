# CoachSnapshot

Target-assignment snapshot. Own pay and contract fields describe that assignment only. Separate latest_known_* fields provide authorized earlier pay with its original year, using the same consecutive-job rule as search. Older 990 base and total are display context; they do not replace current fields, record, income reports or assistant pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_known_fallback** | **bool** | True when the row&#39;s position has no usable annual total but an earlier season of the same unbroken job (same coach, school, sport and position types in every season between) does, and no season since that record carries an hourly record or conflicting positions, so the latest_known_* fields carry that older record as display-only context. It never changes compensation_cents, the comp filters, the compensation sort or comp_stats, and the latest_compensation_* columns behind it are not accepted as filter or sort inputs. The whole latest_known_* group is absent without compensation access. | [optional] 
**latest_known_compensation_cents** | **int** | Total of that older record in cents; null unless latest_known_fallback. | [optional] 
**latest_known_base_salary_cents** | **int** | Base salary of that older record in cents; null unless latest_known_fallback. | [optional] 
**latest_known_compensation_type** | **str** | Compensation type as stored on that older record; null unless latest_known_fallback, and null when the record stores no type (the same raw reading as compensation_type). | [optional] 
**latest_known_source_year** | **int** | End year of the season the older record&#39;s position belongs to (2024 means 2023–24); null unless latest_known_fallback. Always earlier than the target assignment&#39;s season. | [optional] 
**latest_known_source_compensation_id** | **int** | The older compensation record&#39;s id; null unless latest_known_fallback. | [optional] 
**latest_known_source_raw_contract_id** | **int** | The document behind the older record, present only when one is on file and the viewer may open it. Distinct from raw_contract_id, which stays the current position&#39;s contract document. | [optional] 
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


