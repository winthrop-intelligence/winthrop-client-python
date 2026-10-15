# AdminCoachContractQc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**start_on** | **date** |  | [optional] 
**end_on** | **date** |  | [optional] 
**at_will** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**compensation_years** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_contract_qc import AdminCoachContractQc

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachContractQc from a JSON string
admin_coach_contract_qc_instance = AdminCoachContractQc.from_json(json)
# print the JSON string representation of the object
print(AdminCoachContractQc.to_json())

# convert the object into a dict
admin_coach_contract_qc_dict = admin_coach_contract_qc_instance.to_dict()
# create an instance of AdminCoachContractQc from a dict
admin_coach_contract_qc_from_dict = AdminCoachContractQc.from_dict(admin_coach_contract_qc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


