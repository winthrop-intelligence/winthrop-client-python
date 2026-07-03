# FoiaRequestedItemStatusBreakdownMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of_date** | **date** |  | [optional] 
**generated_at** | **datetime** |  | [optional] 
**timezone** | **str** |  | [optional] 
**filters_applied** | **Dict[str, object]** |  | [optional] 
**total_groups** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_requested_item_status_breakdown_meta import FoiaRequestedItemStatusBreakdownMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaRequestedItemStatusBreakdownMeta from a JSON string
foia_requested_item_status_breakdown_meta_instance = FoiaRequestedItemStatusBreakdownMeta.from_json(json)
# print the JSON string representation of the object
print(FoiaRequestedItemStatusBreakdownMeta.to_json())

# convert the object into a dict
foia_requested_item_status_breakdown_meta_dict = foia_requested_item_status_breakdown_meta_instance.to_dict()
# create an instance of FoiaRequestedItemStatusBreakdownMeta from a dict
foia_requested_item_status_breakdown_meta_from_dict = FoiaRequestedItemStatusBreakdownMeta.from_dict(foia_requested_item_status_breakdown_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


