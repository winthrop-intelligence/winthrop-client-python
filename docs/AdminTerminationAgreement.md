# AdminTerminationAgreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**coach** | [**AdminTerminationAgreementCoach**](AdminTerminationAgreementCoach.md) |  | [optional] 
**raw_contract** | [**AdminTerminationAgreementRawContract**](AdminTerminationAgreementRawContract.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_termination_agreement import AdminTerminationAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of AdminTerminationAgreement from a JSON string
admin_termination_agreement_instance = AdminTerminationAgreement.from_json(json)
# print the JSON string representation of the object
print(AdminTerminationAgreement.to_json())

# convert the object into a dict
admin_termination_agreement_dict = admin_termination_agreement_instance.to_dict()
# create an instance of AdminTerminationAgreement from a dict
admin_termination_agreement_from_dict = AdminTerminationAgreement.from_dict(admin_termination_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


