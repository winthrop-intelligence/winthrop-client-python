# ContractTermsSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rendition_sha256** | **str** | SHA-256 (hex) of the OCR text the terms were read from (the text returned by GET /raw_contracts/{id}/ocr_text) | 
**run_id** | **str** | The extraction run that produced the terms | 
**extracted_at** | **datetime** | When the terms were extracted (ISO8601) | 
**method** | **str** | How the terms were extracted and checked | 

## Example

```python
from winthrop_client_python.models.contract_terms_source import ContractTermsSource

# TODO update the JSON string below
json = "{}"
# create an instance of ContractTermsSource from a JSON string
contract_terms_source_instance = ContractTermsSource.from_json(json)
# print the JSON string representation of the object
print(ContractTermsSource.to_json())

# convert the object into a dict
contract_terms_source_dict = contract_terms_source_instance.to_dict()
# create an instance of ContractTermsSource from a dict
contract_terms_source_from_dict = ContractTermsSource.from_dict(contract_terms_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


