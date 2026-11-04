# CreateContractDirectUploadRequestBlob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**byte_size** | **int** |  | 
**checksum** | **str** | Base64 MD5 of the file | 
**content_type** | **str** |  | 

## Example

```python
from winthrop_client_python.models.create_contract_direct_upload_request_blob import CreateContractDirectUploadRequestBlob

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractDirectUploadRequestBlob from a JSON string
create_contract_direct_upload_request_blob_instance = CreateContractDirectUploadRequestBlob.from_json(json)
# print the JSON string representation of the object
print(CreateContractDirectUploadRequestBlob.to_json())

# convert the object into a dict
create_contract_direct_upload_request_blob_dict = create_contract_direct_upload_request_blob_instance.to_dict()
# create an instance of CreateContractDirectUploadRequestBlob from a dict
create_contract_direct_upload_request_blob_from_dict = CreateContractDirectUploadRequestBlob.from_dict(create_contract_direct_upload_request_blob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


