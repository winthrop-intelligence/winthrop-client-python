# EarnedIncentiveFields

The writable fields of an earned incentive (WINAD-10637). Values are earned under the contract, not proof of payment. Owner rulings - an amendment that restates pay ends an earned raise at its effective date (effective_through + ended_by_contract_id); a bonus paid on achievement but vesting later is earned, with the vesting date in effective_from; facts only the school holds stay unresolved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**raw_contract_id** | **int** | The contract the incentive item comes from | [optional] 
**season_id** | **int** | The team season (school + sport + year) the result happened in | [optional] 
**item_id** | **str** | The contract reader&#39;s stable id for the item, unique within the contract (at most 255 characters) | [optional] 
**kind** | **str** | bonus is one-time, raise is an ongoing pay increase, non_cash is e.g. a term extension | [optional] 
**provision_quote** | **str** | The contract language | [optional] 
**status** | **str** | superseded means replaced by a later amendment | [optional] 
**amount_cents** | **int** | Bonus - the amount; raise - the annual increase. Required for an earned bonus or raise; 0 for a not_earned one (the would-be pay goes in potential_amount_cents); null when unresolved, superseded or non_cash. | [optional] 
**potential_amount_cents** | **int** | What the item would pay if earned | [optional] 
**effective_from** | **date** | Raises - the first date the increase applies; vesting bonuses - the vesting date | [optional] 
**effective_through** | **date** | Raises - the last date it applies (contract end, or the day before an amendment that restates pay). On or after effective_from. | [optional] 
**ended_by_contract_id** | **int** | The amendment (raw contract) that ended an earned raise; needs effective_through | [optional] 
**term_change** | [**EarnedIncentiveFieldsTermChange**](EarnedIncentiveFieldsTermChange.md) |  | [optional] 
**missing_fact** | **str** | Required for unresolved items - exactly what is missing | [optional] 
**rationale** | **str** | Short reason | [optional] 
**result_ids** | **List[int]** | The team_season_result ids relied on (may be empty). Each must name an existing team_season_result, from any season, when the row is saved. | [optional] 
**input_id** | **str** | Hash of the exact inputs (terms, results, rulings) both runs decided from | [optional] 
**coverage** | **str** | Set when the contract names a document the PDF lacks | [optional] 
**missing_documents** | **List[str]** | The documents coverage refers to; required with coverage, null without it | [optional] 
**verification_method** | **str** |  | [optional] 
**approved_by_id** | **int** | The person (WinAD user) who approved this exact payload before it was written. Required on write; null only after that user is deleted. | [optional] 
**approved_at** | **datetime** | When the payload was approved, with seconds (at most 6 fraction digits) and an explicit offset (Z or +/-hh:mm, at most 14 hours); a real calendar date, not in the future | [optional] 

## Example

```python
from winthrop_client_python.models.earned_incentive_fields import EarnedIncentiveFields

# TODO update the JSON string below
json = "{}"
# create an instance of EarnedIncentiveFields from a JSON string
earned_incentive_fields_instance = EarnedIncentiveFields.from_json(json)
# print the JSON string representation of the object
print(EarnedIncentiveFields.to_json())

# convert the object into a dict
earned_incentive_fields_dict = earned_incentive_fields_instance.to_dict()
# create an instance of EarnedIncentiveFields from a dict
earned_incentive_fields_from_dict = EarnedIncentiveFields.from_dict(earned_incentive_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


