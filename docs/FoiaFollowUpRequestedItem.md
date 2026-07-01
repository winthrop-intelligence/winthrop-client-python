# FoiaFollowUpRequestedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_item_id** | **int** |  | [optional] 
**requestable_type** | **str** |  | [optional] 
**requestable_id** | **int** |  | [optional] 
**requestable_data** | [**FoiaFollowUpRequestableData**](FoiaFollowUpRequestableData.md) |  | [optional] 
**type_display** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**status_changed_at** | **datetime** |  | [optional] 
**previous_status** | **str** |  | [optional] 
**received_at** | **datetime** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**ri_note_id** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**note_updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_follow_up_requested_item import FoiaFollowUpRequestedItem

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowUpRequestedItem from a JSON string
foia_follow_up_requested_item_instance = FoiaFollowUpRequestedItem.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowUpRequestedItem.to_json())

# convert the object into a dict
foia_follow_up_requested_item_dict = foia_follow_up_requested_item_instance.to_dict()
# create an instance of FoiaFollowUpRequestedItem from a dict
foia_follow_up_requested_item_from_dict = FoiaFollowUpRequestedItem.from_dict(foia_follow_up_requested_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


