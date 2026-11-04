# CreateContractDirectUpload200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_id** | **str** |  | [optional] 
**direct_upload** | [**CreateContractDirectUpload200ResponseDirectUpload**](CreateContractDirectUpload200ResponseDirectUpload.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_contract_direct_upload200_response import CreateContractDirectUpload200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractDirectUpload200Response from a JSON string
create_contract_direct_upload200_response_instance = CreateContractDirectUpload200Response.from_json(json)
# print the JSON string representation of the object
print(CreateContractDirectUpload200Response.to_json())

# convert the object into a dict
create_contract_direct_upload200_response_dict = create_contract_direct_upload200_response_instance.to_dict()
# create an instance of CreateContractDirectUpload200Response from a dict
create_contract_direct_upload200_response_from_dict = CreateContractDirectUpload200Response.from_dict(create_contract_direct_upload200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


