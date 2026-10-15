# AdminCoachContractsQcListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_contracts_qc_list_meta import AdminCoachContractsQcListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachContractsQcListMeta from a JSON string
admin_coach_contracts_qc_list_meta_instance = AdminCoachContractsQcListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminCoachContractsQcListMeta.to_json())

# convert the object into a dict
admin_coach_contracts_qc_list_meta_dict = admin_coach_contracts_qc_list_meta_instance.to_dict()
# create an instance of AdminCoachContractsQcListMeta from a dict
admin_coach_contracts_qc_list_meta_from_dict = AdminCoachContractsQcListMeta.from_dict(admin_coach_contracts_qc_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


