# CreateAdminContractRequestRawContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uploaded_data** | **bytearray** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_contract_request_raw_contract import CreateAdminContractRequestRawContract

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminContractRequestRawContract from a JSON string
create_admin_contract_request_raw_contract_instance = CreateAdminContractRequestRawContract.from_json(json)
# print the JSON string representation of the object
print(CreateAdminContractRequestRawContract.to_json())

# convert the object into a dict
create_admin_contract_request_raw_contract_dict = create_admin_contract_request_raw_contract_instance.to_dict()
# create an instance of CreateAdminContractRequestRawContract from a dict
create_admin_contract_request_raw_contract_from_dict = CreateAdminContractRequestRawContract.from_dict(create_admin_contract_request_raw_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


