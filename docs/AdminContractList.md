# AdminContractList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminCoachContractsQcListMeta**](AdminCoachContractsQcListMeta.md) |  | [optional] 
**data** | [**List[AdminContract]**](AdminContract.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_contract_list import AdminContractList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContractList from a JSON string
admin_contract_list_instance = AdminContractList.from_json(json)
# print the JSON string representation of the object
print(AdminContractList.to_json())

# convert the object into a dict
admin_contract_list_dict = admin_contract_list_instance.to_dict()
# create an instance of AdminContractList from a dict
admin_contract_list_from_dict = AdminContractList.from_dict(admin_contract_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


