# AdminCoachContractsUploadIndexMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_headers** | **List[str]** |  | [optional] 
**optional_headers** | **List[str]** |  | [optional] 
**jobs** | [**List[AdminCoachContractJob]**](AdminCoachContractJob.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_contracts_upload_index_meta import AdminCoachContractsUploadIndexMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachContractsUploadIndexMeta from a JSON string
admin_coach_contracts_upload_index_meta_instance = AdminCoachContractsUploadIndexMeta.from_json(json)
# print the JSON string representation of the object
print(AdminCoachContractsUploadIndexMeta.to_json())

# convert the object into a dict
admin_coach_contracts_upload_index_meta_dict = admin_coach_contracts_upload_index_meta_instance.to_dict()
# create an instance of AdminCoachContractsUploadIndexMeta from a dict
admin_coach_contracts_upload_index_meta_from_dict = AdminCoachContractsUploadIndexMeta.from_dict(admin_coach_contracts_upload_index_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


