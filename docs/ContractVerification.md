# ContractVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seasons** | **List[int]** | Integer season-ending years (2025-26 is 2026), stored sorted and deduplicated. Strings and fractional numbers are rejected. Compensation rows need not exist. | 
**verified_at** | **datetime** | Check time; defaults to now when omitted. May be backdated, never future-dated. | 
**result** | **str** |  | 
**method** | **str** |  | 
**agent_run_id** | **str** | Required for agent events. A new check must use a new run id. | [optional] 
**evidence_url** | **str** | HTTP(S) evidence link; required for passed and mismatch results. | [optional] 
**reason** | **str** | Only set on revoked events. | [optional] 
**approval_quote** | **str** | Only set on revoked events. | [optional] 
**id** | **int** |  | 
**contract_id** | **int** |  | 
**raw_contract_id** | **int** | Checked PDF; becomes null when that RawContract is deleted. | 
**coach_id** | **int** |  | 
**verified_by_id** | **int** | User owning the token at creation; null after that user is deleted. | 
**created_at** | **datetime** | When the event was recorded, independent of verified_at. | 

## Example

```python
from winthrop_client_python.models.contract_verification import ContractVerification

# TODO update the JSON string below
json = "{}"
# create an instance of ContractVerification from a JSON string
contract_verification_instance = ContractVerification.from_json(json)
# print the JSON string representation of the object
print(ContractVerification.to_json())

# convert the object into a dict
contract_verification_dict = contract_verification_instance.to_dict()
# create an instance of ContractVerification from a dict
contract_verification_from_dict = ContractVerification.from_dict(contract_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


