# UserActivitySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**month** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**activity_count** | **int** |  | [optional] 
**user_count** | **int** |  | [optional] 
**active_user_count** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**school_count** | **int** |  | [optional] 
**active_school_count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.user_activity_summary import UserActivitySummary

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivitySummary from a JSON string
user_activity_summary_instance = UserActivitySummary.from_json(json)
# print the JSON string representation of the object
print(UserActivitySummary.to_json())

# convert the object into a dict
user_activity_summary_dict = user_activity_summary_instance.to_dict()
# create an instance of UserActivitySummary from a dict
user_activity_summary_from_dict = UserActivitySummary.from_dict(user_activity_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


