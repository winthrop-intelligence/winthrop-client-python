# AdminTerminationAgreementList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminTerminationAgreement]**](AdminTerminationAgreement.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_termination_agreement_list import AdminTerminationAgreementList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminTerminationAgreementList from a JSON string
admin_termination_agreement_list_instance = AdminTerminationAgreementList.from_json(json)
# print the JSON string representation of the object
print(AdminTerminationAgreementList.to_json())

# convert the object into a dict
admin_termination_agreement_list_dict = admin_termination_agreement_list_instance.to_dict()
# create an instance of AdminTerminationAgreementList from a dict
admin_termination_agreement_list_from_dict = AdminTerminationAgreementList.from_dict(admin_termination_agreement_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


