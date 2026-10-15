# CreateAdminContractRequestContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_on** | **date** |  | [optional] 
**end_on** | **date** |  | [optional] 
**at_will** | **bool** |  | [optional] 
**pending** | **bool** | Pending contracts may omit dates and cannot link compensation. | [optional] 
**contingent_change** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_contract_request_contract import CreateAdminContractRequestContract

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminContractRequestContract from a JSON string
create_admin_contract_request_contract_instance = CreateAdminContractRequestContract.from_json(json)
# print the JSON string representation of the object
print(CreateAdminContractRequestContract.to_json())

# convert the object into a dict
create_admin_contract_request_contract_dict = create_admin_contract_request_contract_instance.to_dict()
# create an instance of CreateAdminContractRequestContract from a dict
create_admin_contract_request_contract_from_dict = CreateAdminContractRequestContract.from_dict(create_admin_contract_request_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


