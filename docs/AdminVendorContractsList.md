# AdminVendorContractsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminVendorContract]**](AdminVendorContract.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_vendor_contracts_list import AdminVendorContractsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminVendorContractsList from a JSON string
admin_vendor_contracts_list_instance = AdminVendorContractsList.from_json(json)
# print the JSON string representation of the object
print(AdminVendorContractsList.to_json())

# convert the object into a dict
admin_vendor_contracts_list_dict = admin_vendor_contracts_list_instance.to_dict()
# create an instance of AdminVendorContractsList from a dict
admin_vendor_contracts_list_from_dict = AdminVendorContractsList.from_dict(admin_vendor_contracts_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


