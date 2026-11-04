# DealVerificationRevocationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**approval_quote** | **str** |  | 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

## Example

```python
from winthrop_client_python.models.deal_verification_revocation_input import DealVerificationRevocationInput

# TODO update the JSON string below
json = "{}"
# create an instance of DealVerificationRevocationInput from a JSON string
deal_verification_revocation_input_instance = DealVerificationRevocationInput.from_json(json)
# print the JSON string representation of the object
print(DealVerificationRevocationInput.to_json())

# convert the object into a dict
deal_verification_revocation_input_dict = deal_verification_revocation_input_instance.to_dict()
# create an instance of DealVerificationRevocationInput from a dict
deal_verification_revocation_input_from_dict = DealVerificationRevocationInput.from_dict(deal_verification_revocation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


