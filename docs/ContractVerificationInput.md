# ContractVerificationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seasons** | **List[int]** | Integer season-ending years (2025-26 is 2026), stored sorted and deduplicated. Strings and fractional numbers are rejected. Compensation rows need not exist. | 
**verified_at** | **datetime** | Check time; defaults to now when omitted. May be backdated, never future-dated. | [optional] 
**result** | **str** |  | 
**method** | **str** |  | 
**agent_run_id** | **str** | Required for agent events. A new check must use a new run id. | [optional] 
**evidence_url** | **str** | HTTP(S) evidence link; required for passed and mismatch results. | [optional] 
**batch_id** | **str** | Optional label of the posting batch that made this event, so one batch can be found later (GET /contract_verifications?q[batch_id_eq]&#x3D;...). Trimmed; blank is the same as omitted; at most 100 characters, no control characters. Not part of the retry payload: an agent retry that differs only in batch_id or code_version is answered with the original event. | [optional] 
**code_version** | **str** | Optional commit SHA (7 to 40 hex digits) of the code that posted the event; stored in lower case. Blank is the same as omitted. | [optional] 

## Example

```python
from winthrop_client_python.models.contract_verification_input import ContractVerificationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ContractVerificationInput from a JSON string
contract_verification_input_instance = ContractVerificationInput.from_json(json)
# print the JSON string representation of the object
print(ContractVerificationInput.to_json())

# convert the object into a dict
contract_verification_input_dict = contract_verification_input_instance.to_dict()
# create an instance of ContractVerificationInput from a dict
contract_verification_input_from_dict = ContractVerificationInput.from_dict(contract_verification_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


