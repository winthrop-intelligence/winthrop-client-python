# RawContractUploaded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The new RawContract&#39;s id (the raw_contract_id of an income report) | 
**filename** | **str** | The uploaded PDF&#39;s filename | 
**content_type** | **str** | The stored content type | 
**file_size** | **int** | The stored file&#39;s size in bytes | 
**coach_id** | **int** |  | 
**school_id** | **int** | The school the document is filed under (the one sent, else the coach&#39;s current school) | 
**start_on** | **date** | The dated contract&#39;s start; null when no Contract was filed | 
**end_on** | **date** | The dated contract&#39;s end; null when no Contract was filed | 
**contract_id** | **int** | The Coach contract filed with the dates; null when none was filed | 

## Example

```python
from winthrop_client_python.models.raw_contract_uploaded import RawContractUploaded

# TODO update the JSON string below
json = "{}"
# create an instance of RawContractUploaded from a JSON string
raw_contract_uploaded_instance = RawContractUploaded.from_json(json)
# print the JSON string representation of the object
print(RawContractUploaded.to_json())

# convert the object into a dict
raw_contract_uploaded_dict = raw_contract_uploaded_instance.to_dict()
# create an instance of RawContractUploaded from a dict
raw_contract_uploaded_from_dict = RawContractUploaded.from_dict(raw_contract_uploaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


