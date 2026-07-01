# FoiaFollowUpRecentReceivedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_item_id** | **int** |  | [optional] 
**requestable_type** | **str** |  | [optional] 
**requestable_id** | **int** |  | [optional] 
**requestable_data** | [**FoiaFollowUpRequestableData**](FoiaFollowUpRequestableData.md) |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_changed_at** | **datetime** |  | [optional] 
**received_at** | **datetime** |  | [optional] 
**previous_status** | **str** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_follow_up_recent_received_item import FoiaFollowUpRecentReceivedItem

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowUpRecentReceivedItem from a JSON string
foia_follow_up_recent_received_item_instance = FoiaFollowUpRecentReceivedItem.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowUpRecentReceivedItem.to_json())

# convert the object into a dict
foia_follow_up_recent_received_item_dict = foia_follow_up_recent_received_item_instance.to_dict()
# create an instance of FoiaFollowUpRecentReceivedItem from a dict
foia_follow_up_recent_received_item_from_dict = FoiaFollowUpRecentReceivedItem.from_dict(foia_follow_up_recent_received_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


