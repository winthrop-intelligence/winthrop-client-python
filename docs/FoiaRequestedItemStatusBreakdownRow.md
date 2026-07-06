# FoiaRequestedItemStatusBreakdownRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **date** | Start of the calendar bucket derived from requested_items.updated_at; null when updated_period is not in group_by. | [optional] 
**requestable_type** | **str** | Null when requestable_type is not in group_by. | [optional] 
**requestable_type_display** | **str** |  | [optional] 
**pending_count** | **int** |  | [optional] 
**received_count** | **int** |  | [optional] 
**not_available_count** | **int** |  | [optional] 
**accounted_for_count** | **int** | received_count + not_available_count | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_requested_item_status_breakdown_row import FoiaRequestedItemStatusBreakdownRow

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaRequestedItemStatusBreakdownRow from a JSON string
foia_requested_item_status_breakdown_row_instance = FoiaRequestedItemStatusBreakdownRow.from_json(json)
# print the JSON string representation of the object
print(FoiaRequestedItemStatusBreakdownRow.to_json())

# convert the object into a dict
foia_requested_item_status_breakdown_row_dict = foia_requested_item_status_breakdown_row_instance.to_dict()
# create an instance of FoiaRequestedItemStatusBreakdownRow from a dict
foia_requested_item_status_breakdown_row_from_dict = FoiaRequestedItemStatusBreakdownRow.from_dict(foia_requested_item_status_breakdown_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


