# CreateAdminCoachMergeLogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_coach_id** | **int** |  | [optional] 
**duplicate_coach_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_coach_merge_log_request import CreateAdminCoachMergeLogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminCoachMergeLogRequest from a JSON string
create_admin_coach_merge_log_request_instance = CreateAdminCoachMergeLogRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminCoachMergeLogRequest.to_json())

# convert the object into a dict
create_admin_coach_merge_log_request_dict = create_admin_coach_merge_log_request_instance.to_dict()
# create an instance of CreateAdminCoachMergeLogRequest from a dict
create_admin_coach_merge_log_request_from_dict = CreateAdminCoachMergeLogRequest.from_dict(create_admin_coach_merge_log_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


