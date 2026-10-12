# DeskQueueEngagementError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from winthrop_client_python.models.desk_queue_engagement_error import DeskQueueEngagementError

# TODO update the JSON string below
json = "{}"
# create an instance of DeskQueueEngagementError from a JSON string
desk_queue_engagement_error_instance = DeskQueueEngagementError.from_json(json)
# print the JSON string representation of the object
print(DeskQueueEngagementError.to_json())

# convert the object into a dict
desk_queue_engagement_error_dict = desk_queue_engagement_error_instance.to_dict()
# create an instance of DeskQueueEngagementError from a dict
desk_queue_engagement_error_from_dict = DeskQueueEngagementError.from_dict(desk_queue_engagement_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


