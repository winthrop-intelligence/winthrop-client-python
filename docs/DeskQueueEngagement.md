# DeskQueueEngagement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_uuid** | **UUID** |  | 
**status** | **str** |  | 
**unique_viewers** | **int** |  | 
**total_opens** | **int** |  | 
**last_viewed_at** | **datetime** | Latest qualifying customer open in the effective interval, across every viewer/version; null at zero. | 
**refreshed_at** | **datetime** |  | 
**period** | [**DeskQueueEngagementPeriod**](DeskQueueEngagementPeriod.md) |  | 
**coverage** | [**DeskQueueEngagementCoverage**](DeskQueueEngagementCoverage.md) |  | 
**error** | [**DeskQueueEngagementError**](DeskQueueEngagementError.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_queue_engagement import DeskQueueEngagement

# TODO update the JSON string below
json = "{}"
# create an instance of DeskQueueEngagement from a JSON string
desk_queue_engagement_instance = DeskQueueEngagement.from_json(json)
# print the JSON string representation of the object
print(DeskQueueEngagement.to_json())

# convert the object into a dict
desk_queue_engagement_dict = desk_queue_engagement_instance.to_dict()
# create an instance of DeskQueueEngagement from a dict
desk_queue_engagement_from_dict = DeskQueueEngagement.from_dict(desk_queue_engagement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


