# CreateContractDirectUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blob** | [**CreateContractDirectUploadRequestBlob**](CreateContractDirectUploadRequestBlob.md) |  | 

## Example

```python
from winthrop_client_python.models.create_contract_direct_upload_request import CreateContractDirectUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractDirectUploadRequest from a JSON string
create_contract_direct_upload_request_instance = CreateContractDirectUploadRequest.from_json(json)
# print the JSON string representation of the object
print(CreateContractDirectUploadRequest.to_json())

# convert the object into a dict
create_contract_direct_upload_request_dict = create_contract_direct_upload_request_instance.to_dict()
# create an instance of CreateContractDirectUploadRequest from a dict
create_contract_direct_upload_request_from_dict = CreateContractDirectUploadRequest.from_dict(create_contract_direct_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


