# RawContractTerms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the RawContract | 
**contract_terms** | [**ContractTerms**](ContractTerms.md) |  | 
**contract_terms_stale** | **bool** | True when contract_terms is present and source.rendition_sha256 no longer matches the SHA-256 of the current OCR text (the contract was re-OCR&#39;d since the terms were read). The terms are kept; re-check and store them again to clear it. | 

## Example

```python
from winthrop_client_python.models.raw_contract_terms import RawContractTerms

# TODO update the JSON string below
json = "{}"
# create an instance of RawContractTerms from a JSON string
raw_contract_terms_instance = RawContractTerms.from_json(json)
# print the JSON string representation of the object
print(RawContractTerms.to_json())

# convert the object into a dict
raw_contract_terms_dict = raw_contract_terms_instance.to_dict()
# create an instance of RawContractTerms from a dict
raw_contract_terms_from_dict = RawContractTerms.from_dict(raw_contract_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


