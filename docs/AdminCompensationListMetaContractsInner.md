# AdminCompensationListMetaContractsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**pending** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**verified_by** | **str** | \&quot;&lt;user&gt; at &lt;time&gt;\&quot; of the latest verification | [optional] 
**raw_contract_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_compensation_list_meta_contracts_inner import AdminCompensationListMetaContractsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCompensationListMetaContractsInner from a JSON string
admin_compensation_list_meta_contracts_inner_instance = AdminCompensationListMetaContractsInner.from_json(json)
# print the JSON string representation of the object
print(AdminCompensationListMetaContractsInner.to_json())

# convert the object into a dict
admin_compensation_list_meta_contracts_inner_dict = admin_compensation_list_meta_contracts_inner_instance.to_dict()
# create an instance of AdminCompensationListMetaContractsInner from a dict
admin_compensation_list_meta_contracts_inner_from_dict = AdminCompensationListMetaContractsInner.from_dict(admin_compensation_list_meta_contracts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


