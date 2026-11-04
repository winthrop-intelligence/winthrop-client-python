# DealVerificationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified_at** | **datetime** | Check time; defaults to now when omitted. May be backdated, never future-dated. | [optional] 
**result** | **str** |  | 
**method** | **str** |  | 
**agent_run_id** | **str** | Required for agent events. A new check must use a new run id. | [optional] 
**evidence_url** | **str** | HTTP(S) evidence link; required for passed and mismatch results. | [optional] 
**batch_id** | **str** | Optional label of the posting batch (GET /deal_verifications?q[batch_id_eq]&#x3D;...). Trimmed; blank is the same as omitted; no control characters. Not part of the retry payload. | [optional] 
**code_version** | **str** | Optional commit SHA (7 to 40 hex digits) of the code that posted the event; stored in lower case. Not part of the retry payload. | [optional] 

## Example

```python
from winthrop_client_python.models.deal_verification_input import DealVerificationInput

# TODO update the JSON string below
json = "{}"
# create an instance of DealVerificationInput from a JSON string
deal_verification_input_instance = DealVerificationInput.from_json(json)
# print the JSON string representation of the object
print(DealVerificationInput.to_json())

# convert the object into a dict
deal_verification_input_dict = deal_verification_input_instance.to_dict()
# create an instance of DealVerificationInput from a dict
deal_verification_input_from_dict = DealVerificationInput.from_dict(deal_verification_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


