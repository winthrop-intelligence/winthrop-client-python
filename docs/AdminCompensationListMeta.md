# AdminCompensationListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** |  | [optional] 
**contract_status_options** | [**List[AdminCompensationListMetaContractStatusOptionsInner]**](AdminCompensationListMetaContractStatusOptionsInner.md) |  | [optional] 
**coach_contract_options** | [**List[AdminCompensationListMetaCoachContractOptionsInner]**](AdminCompensationListMetaCoachContractOptionsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_compensation_list_meta import AdminCompensationListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCompensationListMeta from a JSON string
admin_compensation_list_meta_instance = AdminCompensationListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminCompensationListMeta.to_json())

# convert the object into a dict
admin_compensation_list_meta_dict = admin_compensation_list_meta_instance.to_dict()
# create an instance of AdminCompensationListMeta from a dict
admin_compensation_list_meta_from_dict = AdminCompensationListMeta.from_dict(admin_compensation_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


