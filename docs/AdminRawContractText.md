# AdminRawContractText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**has_file** | **bool** |  | [optional] 
**has_ocr_file** | **bool** |  | [optional] 
**best_extracted_text** | **str** |  | [optional] 
**ocr_text** | **str** |  | [optional] 
**unstract_pdf_text** | **str** |  | [optional] 
**layout_preserved_pdf_text** | **str** |  | [optional] 
**text_unstract_state** | **str** |  | [optional] 
**text_unstract_error_message** | **str** |  | [optional] 
**layout_preserved_unstract_state** | **str** |  | [optional] 
**layout_preserved_unstract_error_message** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_raw_contract_text import AdminRawContractText

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRawContractText from a JSON string
admin_raw_contract_text_instance = AdminRawContractText.from_json(json)
# print the JSON string representation of the object
print(AdminRawContractText.to_json())

# convert the object into a dict
admin_raw_contract_text_dict = admin_raw_contract_text_instance.to_dict()
# create an instance of AdminRawContractText from a dict
admin_raw_contract_text_from_dict = AdminRawContractText.from_dict(admin_raw_contract_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


