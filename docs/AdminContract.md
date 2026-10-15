# AdminContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | **bool** |  | [optional] 
**id** | **int** |  | 
**start_on** | **date** |  | [optional] 
**end_on** | **date** |  | [optional] 
**at_will** | **bool** |  | [optional] 
**contingent_change** | **bool** |  | [optional] 
**executed_on** | **date** |  | [optional] 
**expires_on** | **date** |  | [optional] 
**verified** | **bool** |  | [optional] 
**drive_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach** | [**AdminContractCoach**](AdminContractCoach.md) |  | [optional] 
**raw_contract** | [**AdminContractRawContract**](AdminContractRawContract.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_contract import AdminContract

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContract from a JSON string
admin_contract_instance = AdminContract.from_json(json)
# print the JSON string representation of the object
print(AdminContract.to_json())

# convert the object into a dict
admin_contract_dict = admin_contract_instance.to_dict()
# create an instance of AdminContract from a dict
admin_contract_from_dict = AdminContract.from_dict(admin_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


