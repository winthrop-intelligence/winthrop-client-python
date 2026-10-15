# AdminCoachContractsQcList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminCoachContractsQcListMeta**](AdminCoachContractsQcListMeta.md) |  | [optional] 
**data** | [**List[AdminCoachContractQc]**](AdminCoachContractQc.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_contracts_qc_list import AdminCoachContractsQcList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachContractsQcList from a JSON string
admin_coach_contracts_qc_list_instance = AdminCoachContractsQcList.from_json(json)
# print the JSON string representation of the object
print(AdminCoachContractsQcList.to_json())

# convert the object into a dict
admin_coach_contracts_qc_list_dict = admin_coach_contracts_qc_list_instance.to_dict()
# create an instance of AdminCoachContractsQcList from a dict
admin_coach_contracts_qc_list_from_dict = AdminCoachContractsQcList.from_dict(admin_coach_contracts_qc_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


