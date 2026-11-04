# DealVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**deal_id** | **int** |  | 
**verified_at** | **datetime** |  | 
**result** | **str** |  | 
**method** | **str** |  | 
**verified_by_id** | **int** | Null when the verifier user was deleted. | [optional] 
**agent_run_id** | **str** |  | [optional] 
**evidence_url** | **str** |  | [optional] 
**reason** | **str** | Only set on revoked events. | [optional] 
**approval_quote** | **str** | Only set on revoked events. | [optional] 
**batch_id** | **str** |  | [optional] 
**code_version** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.deal_verification import DealVerification

# TODO update the JSON string below
json = "{}"
# create an instance of DealVerification from a JSON string
deal_verification_instance = DealVerification.from_json(json)
# print the JSON string representation of the object
print(DealVerification.to_json())

# convert the object into a dict
deal_verification_dict = deal_verification_instance.to_dict()
# create an instance of DealVerification from a dict
deal_verification_from_dict = DealVerification.from_dict(deal_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


