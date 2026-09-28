# GetRawContractOcrText200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**text** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from winthrop_client_python.models.get_raw_contract_ocr_text200_response import GetRawContractOcrText200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawContractOcrText200Response from a JSON string
get_raw_contract_ocr_text200_response_instance = GetRawContractOcrText200Response.from_json(json)
# print the JSON string representation of the object
print(GetRawContractOcrText200Response.to_json())

# convert the object into a dict
get_raw_contract_ocr_text200_response_dict = get_raw_contract_ocr_text200_response_instance.to_dict()
# create an instance of GetRawContractOcrText200Response from a dict
get_raw_contract_ocr_text200_response_from_dict = GetRawContractOcrText200Response.from_dict(get_raw_contract_ocr_text200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


