# ContractCreateOnRawContract

WINAD-10747. Files a published contract on a RawContract that is already in WinAD (no upload).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_contract_id** | **int** | The existing RawContract (a COACH document, not a vendor deal&#39;s or a pending contract&#39;s). Other coaches may already hold a contract on it; this coach may not. | 
**coach_id** | **int** | The coach the contract is for | 
**contractable_type** | **str** |  | 
**start_on** | **date** |  | 
**end_on** | **date** |  | 
**school_id** | **int** | Optional. Must be an existing school and, when the document already has a school, that school. The document is not changed. | [optional] 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history (stored on the audit version, never returned). At most 500 characters after trimming; blank is the same as omitted; longer is refused with 422 (errors.change_note). | [optional] 

## Example

```python
from winthrop_client_python.models.contract_create_on_raw_contract import ContractCreateOnRawContract

# TODO update the JSON string below
json = "{}"
# create an instance of ContractCreateOnRawContract from a JSON string
contract_create_on_raw_contract_instance = ContractCreateOnRawContract.from_json(json)
# print the JSON string representation of the object
print(ContractCreateOnRawContract.to_json())

# convert the object into a dict
contract_create_on_raw_contract_dict = contract_create_on_raw_contract_instance.to_dict()
# create an instance of ContractCreateOnRawContract from a dict
contract_create_on_raw_contract_from_dict = ContractCreateOnRawContract.from_dict(contract_create_on_raw_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


