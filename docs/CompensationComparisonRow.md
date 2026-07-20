# CompensationComparisonRow

One school/match candidate. Compensation and contract fields are only present when the caller's permissions allow them (comp_status is comp_redacted otherwise). Synthesized no_role_match / school_not_accessible rows carry null person fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | Namespaced person id, \&quot;coach:&lt;id&gt;\&quot; or \&quot;administrator:&lt;id&gt;\&quot;. | 
**source** | **str** |  | 
**school_id** | **int** |  | 
**school_name** | **str** |  | 
**school_short_name** | **str** |  | 
**coach_id** | **int** |  | 
**coach_friendly_id** | **str** |  | 
**coach_name** | **str** |  | 
**raw_title** | **str** |  | 
**position_types** | **List[str]** |  | 
**sport_name** | **str** | Null for administrator rows (admin records are not sport-scoped). | 
**year** | **int** |  | 
**match_type** | **str** |  | 
**match_notes** | **str** |  | 
**comp_status** | **str** |  | 
**compensation_cents** | **int** | Total compensation (calculated guaranteed comp) in cents. | [optional] 
**base_salary_cents** | **int** |  | [optional] 
**talent_fee_cents** | **int** |  | [optional] 
**one_time_bonus_cents** | **int** |  | [optional] 
**outside_income_cents** | **int** |  | [optional] 
**deferred_comp_cents** | **int** |  | [optional] 
**compensation_type** | **str** |  | [optional] 
**contract_starts_on** | **date** |  | [optional] 
**contract_expires_on** | **date** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.compensation_comparison_row import CompensationComparisonRow

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationComparisonRow from a JSON string
compensation_comparison_row_instance = CompensationComparisonRow.from_json(json)
# print the JSON string representation of the object
print(CompensationComparisonRow.to_json())

# convert the object into a dict
compensation_comparison_row_dict = compensation_comparison_row_instance.to_dict()
# create an instance of CompensationComparisonRow from a dict
compensation_comparison_row_from_dict = CompensationComparisonRow.from_dict(compensation_comparison_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


