# AdminGameContractUploaderJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**arguments** | **List[object]** |  | [optional] 
**enqueued_at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_game_contract_uploader_job import AdminGameContractUploaderJob

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGameContractUploaderJob from a JSON string
admin_game_contract_uploader_job_instance = AdminGameContractUploaderJob.from_json(json)
# print the JSON string representation of the object
print(AdminGameContractUploaderJob.to_json())

# convert the object into a dict
admin_game_contract_uploader_job_dict = admin_game_contract_uploader_job_instance.to_dict()
# create an instance of AdminGameContractUploaderJob from a dict
admin_game_contract_uploader_job_from_dict = AdminGameContractUploaderJob.from_dict(admin_game_contract_uploader_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


