# CompensationVerificationChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | base_salary_cents, talent_fee, one_time_bonus_cents, relocation_cents, relocation_taxable, deferred_comp_cents, year, coach_id, school_id, contract_id or contract_status_id (the compensation row, or another row of the same contract that was linked or unlinked, or moved into or out of the season: year); row (a row created in the season, or deleted from it); position.season_id, position.coach_id or position.compensation_id; contract.coach_id; raw_contract.file or raw_contract.school_id; or unreadable when the saved data could not be read. | 
**old** | **object** | Value before the change (any JSON value; null when there was none or for &#x60;unreadable&#x60;). For &#x60;row&#x60;: null for a created row, and &#x60;compensation &lt;id&gt;&#x60; (the deleted row&#39;s id) for a deleted one. | 
**new** | **object** | Value after the change (any JSON value; for &#x60;row&#x60;: &#x60;created&#x60; for a created row, null for a deleted one). | 
**at** | **datetime** | When the change was recorded. | 
**user** | [**CompensationVerificationChangeUser**](CompensationVerificationChangeUser.md) |  | 

## Example

```python
from winthrop_client_python.models.compensation_verification_change import CompensationVerificationChange

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationVerificationChange from a JSON string
compensation_verification_change_instance = CompensationVerificationChange.from_json(json)
# print the JSON string representation of the object
print(CompensationVerificationChange.to_json())

# convert the object into a dict
compensation_verification_change_dict = compensation_verification_change_instance.to_dict()
# create an instance of CompensationVerificationChange from a dict
compensation_verification_change_from_dict = CompensationVerificationChange.from_dict(compensation_verification_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


