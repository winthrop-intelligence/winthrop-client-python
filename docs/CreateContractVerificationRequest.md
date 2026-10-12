# CreateContractVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_verification** | [**ContractVerificationInput**](ContractVerificationInput.md) |  | 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

## Example

```python
from winthrop_client_python.models.create_contract_verification_request import CreateContractVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractVerificationRequest from a JSON string
create_contract_verification_request_instance = CreateContractVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateContractVerificationRequest.to_json())

# convert the object into a dict
create_contract_verification_request_dict = create_contract_verification_request_instance.to_dict()
# create an instance of CreateContractVerificationRequest from a dict
create_contract_verification_request_from_dict = CreateContractVerificationRequest.from_dict(create_contract_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


