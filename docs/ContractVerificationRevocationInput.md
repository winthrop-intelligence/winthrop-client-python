# ContractVerificationRevocationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seasons** | **List[int]** |  | 
**reason** | **str** |  | 
**approval_quote** | **str** |  | 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

## Example

```python
from winthrop_client_python.models.contract_verification_revocation_input import ContractVerificationRevocationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ContractVerificationRevocationInput from a JSON string
contract_verification_revocation_input_instance = ContractVerificationRevocationInput.from_json(json)
# print the JSON string representation of the object
print(ContractVerificationRevocationInput.to_json())

# convert the object into a dict
contract_verification_revocation_input_dict = contract_verification_revocation_input_instance.to_dict()
# create an instance of ContractVerificationRevocationInput from a dict
contract_verification_revocation_input_from_dict = ContractVerificationRevocationInput.from_dict(contract_verification_revocation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


