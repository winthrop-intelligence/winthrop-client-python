# ContractVerificationRevocationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seasons** | **List[int]** |  | 
**reason** | **str** |  | 
**approval_quote** | **str** |  | 
**change_note** | **str** | Why this change is being made, for the internal audit history (WINAD-10632). It is stored on the audit version this write creates and is never returned. Blank is the same as omitted; a non-string value is refused with 422 (errors.change_note). It is separate from approval_quote, which is stored on the revocation event itself. | [optional] 

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


