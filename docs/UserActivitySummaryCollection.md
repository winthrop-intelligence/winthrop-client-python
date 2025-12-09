# UserActivitySummaryCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserActivitySummary]**](UserActivitySummary.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.user_activity_summary_collection import UserActivitySummaryCollection

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivitySummaryCollection from a JSON string
user_activity_summary_collection_instance = UserActivitySummaryCollection.from_json(json)
# print the JSON string representation of the object
print(UserActivitySummaryCollection.to_json())

# convert the object into a dict
user_activity_summary_collection_dict = user_activity_summary_collection_instance.to_dict()
# create an instance of UserActivitySummaryCollection from a dict
user_activity_summary_collection_from_dict = UserActivitySummaryCollection.from_dict(user_activity_summary_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


