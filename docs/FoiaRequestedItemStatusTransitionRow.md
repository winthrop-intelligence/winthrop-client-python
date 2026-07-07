# FoiaRequestedItemStatusTransitionRow

A single status transition event. One requested item can appear in multiple rows when its status changed more than once in the window.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_item_id** | **int** |  | [optional] 
**foia_request_id** | **int** |  | [optional] 
**foia_label_id** | **int** |  | [optional] 
**foia_label_name** | **str** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**requestable_type** | **str** |  | [optional] 
**requestable_id** | **int** |  | [optional] 
**from_status** | **str** | Status before the transition; null when the prior value is unknown. Legacy audit rows may contain historical status strings verbatim. | [optional] 
**to_status** | **str** |  | [optional] 
**status_changed_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_requested_item_status_transition_row import FoiaRequestedItemStatusTransitionRow

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaRequestedItemStatusTransitionRow from a JSON string
foia_requested_item_status_transition_row_instance = FoiaRequestedItemStatusTransitionRow.from_json(json)
# print the JSON string representation of the object
print(FoiaRequestedItemStatusTransitionRow.to_json())

# convert the object into a dict
foia_requested_item_status_transition_row_dict = foia_requested_item_status_transition_row_instance.to_dict()
# create an instance of FoiaRequestedItemStatusTransitionRow from a dict
foia_requested_item_status_transition_row_from_dict = FoiaRequestedItemStatusTransitionRow.from_dict(foia_requested_item_status_transition_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


