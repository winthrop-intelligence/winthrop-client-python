# DeskQueueEngagementBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**DeskQueueEngagementBatchMeta**](DeskQueueEngagementBatchMeta.md) |  | 
**data** | [**List[DeskQueueEngagement]**](DeskQueueEngagement.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_queue_engagement_batch import DeskQueueEngagementBatch

# TODO update the JSON string below
json = "{}"
# create an instance of DeskQueueEngagementBatch from a JSON string
desk_queue_engagement_batch_instance = DeskQueueEngagementBatch.from_json(json)
# print the JSON string representation of the object
print(DeskQueueEngagementBatch.to_json())

# convert the object into a dict
desk_queue_engagement_batch_dict = desk_queue_engagement_batch_instance.to_dict()
# create an instance of DeskQueueEngagementBatch from a dict
desk_queue_engagement_batch_from_dict = DeskQueueEngagementBatch.from_dict(desk_queue_engagement_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


