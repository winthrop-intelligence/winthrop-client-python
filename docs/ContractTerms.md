# ContractTerms

One document of structured terms per RawContract (WINAD-10633). Only `schema` and `source` are required and checked; every other key is a term, in a shape set by `schema`, and is stored as sent. Each term carries the quote and page number it was read from in the contract's OCR text. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The terms&#39; shape and version, for example ticketing-terms-v1, pouring-terms-v1 or coach-terms-v1 | 
**source** | [**ContractTermsSource**](ContractTermsSource.md) |  | 

## Example

```python
from winthrop_client_python.models.contract_terms import ContractTerms

# TODO update the JSON string below
json = "{}"
# create an instance of ContractTerms from a JSON string
contract_terms_instance = ContractTerms.from_json(json)
# print the JSON string representation of the object
print(ContractTerms.to_json())

# convert the object into a dict
contract_terms_dict = contract_terms_instance.to_dict()
# create an instance of ContractTerms from a dict
contract_terms_from_dict = ContractTerms.from_dict(contract_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


