# FoiaStatusSummaryRequestedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_item_id** | **int** |  | 
**requestable_type** | **str** |  | 
**status** | **str** | Item-level state. Source states are pending, received and not_available; received and not_available count as accounted for. partial is not an item state (the Ops normalizer additionally tolerates it). | 

## Example

```python
from winthrop_client_python.models.foia_status_summary_requested_item import FoiaStatusSummaryRequestedItem

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaStatusSummaryRequestedItem from a JSON string
foia_status_summary_requested_item_instance = FoiaStatusSummaryRequestedItem.from_json(json)
# print the JSON string representation of the object
print(FoiaStatusSummaryRequestedItem.to_json())

# convert the object into a dict
foia_status_summary_requested_item_dict = foia_status_summary_requested_item_instance.to_dict()
# create an instance of FoiaStatusSummaryRequestedItem from a dict
foia_status_summary_requested_item_from_dict = FoiaStatusSummaryRequestedItem.from_dict(foia_status_summary_requested_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


