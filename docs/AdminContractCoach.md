# AdminContractCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_contract_coach import AdminContractCoach

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContractCoach from a JSON string
admin_contract_coach_instance = AdminContractCoach.from_json(json)
# print the JSON string representation of the object
print(AdminContractCoach.to_json())

# convert the object into a dict
admin_contract_coach_dict = admin_contract_coach_instance.to_dict()
# create an instance of AdminContractCoach from a dict
admin_contract_coach_from_dict = AdminContractCoach.from_dict(admin_contract_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


