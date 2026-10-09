# DeskQueueEngagementPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**requested_from** | **datetime** |  | 
**var_from** | **datetime** |  | 
**to** | **datetime** |  | 
**timezone** | **str** |  | 
**interval** | **str** |  | 
**across_versions** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.desk_queue_engagement_period import DeskQueueEngagementPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of DeskQueueEngagementPeriod from a JSON string
desk_queue_engagement_period_instance = DeskQueueEngagementPeriod.from_json(json)
# print the JSON string representation of the object
print(DeskQueueEngagementPeriod.to_json())

# convert the object into a dict
desk_queue_engagement_period_dict = desk_queue_engagement_period_instance.to_dict()
# create an instance of DeskQueueEngagementPeriod from a dict
desk_queue_engagement_period_from_dict = DeskQueueEngagementPeriod.from_dict(desk_queue_engagement_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


