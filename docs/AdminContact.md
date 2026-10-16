# AdminContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school** | [**IdName**](IdName.md) |  | [optional] 
**sport** | [**AdminCompensationListMetaContractStatusOptionsInner**](AdminCompensationListMetaContractStatusOptionsInner.md) |  | [optional] 
**coach** | [**IdName**](IdName.md) |  | [optional] 
**verified_scheduling_contact** | **bool** |  | [optional] 
**verified_at** | **datetime** |  | [optional] 
**latest_positions** | [**List[AdminContactLatestPositionsInner]**](AdminContactLatestPositionsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_contact import AdminContact

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContact from a JSON string
admin_contact_instance = AdminContact.from_json(json)
# print the JSON string representation of the object
print(AdminContact.to_json())

# convert the object into a dict
admin_contact_dict = admin_contact_instance.to_dict()
# create an instance of AdminContact from a dict
admin_contact_from_dict = AdminContact.from_dict(admin_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


