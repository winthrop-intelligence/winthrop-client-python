# AdminContractRawContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**filename** | **str** |  | [optional] 
**file_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_contract_raw_contract import AdminContractRawContract

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContractRawContract from a JSON string
admin_contract_raw_contract_instance = AdminContractRawContract.from_json(json)
# print the JSON string representation of the object
print(AdminContractRawContract.to_json())

# convert the object into a dict
admin_contract_raw_contract_dict = admin_contract_raw_contract_instance.to_dict()
# create an instance of AdminContractRawContract from a dict
admin_contract_raw_contract_from_dict = AdminContractRawContract.from_dict(admin_contract_raw_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


