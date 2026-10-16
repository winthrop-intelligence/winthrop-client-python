# AdminContractRequestSearchesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminContractRequestSearches]**](AdminContractRequestSearches.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_contract_request_searches_list import AdminContractRequestSearchesList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContractRequestSearchesList from a JSON string
admin_contract_request_searches_list_instance = AdminContractRequestSearchesList.from_json(json)
# print the JSON string representation of the object
print(AdminContractRequestSearchesList.to_json())

# convert the object into a dict
admin_contract_request_searches_list_dict = admin_contract_request_searches_list_instance.to_dict()
# create an instance of AdminContractRequestSearchesList from a dict
admin_contract_request_searches_list_from_dict = AdminContractRequestSearchesList.from_dict(admin_contract_request_searches_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


