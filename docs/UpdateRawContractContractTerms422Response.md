# UpdateRawContractContractTerms422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **Dict[str, List[str]]** | Field paths such as schema, source or source.rendition_sha256 (base for a body that is not an object) mapped to errors. | [optional] 

## Example

```python
from winthrop_client_python.models.update_raw_contract_contract_terms422_response import UpdateRawContractContractTerms422Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRawContractContractTerms422Response from a JSON string
update_raw_contract_contract_terms422_response_instance = UpdateRawContractContractTerms422Response.from_json(json)
# print the JSON string representation of the object
print(UpdateRawContractContractTerms422Response.to_json())

# convert the object into a dict
update_raw_contract_contract_terms422_response_dict = update_raw_contract_contract_terms422_response_instance.to_dict()
# create an instance of UpdateRawContractContractTerms422Response from a dict
update_raw_contract_contract_terms422_response_from_dict = UpdateRawContractContractTerms422Response.from_dict(update_raw_contract_contract_terms422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


