# RequestedItemReviewContextRequestedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | **str** |  | 
**requestable_id** | **int** |  | 
**requestable_type** | **str** |  | 
**type_display** | **str** | Human-readable requested item category as displayed in WinAD. | 
**title** | **str** | Canonical WinAD display title for the requested item. Returns \&quot;Item Deleted\&quot; when the underlying requestable record no longer exists. | 

## Example

```python
from winthrop_client_python.models.requested_item_review_context_requested_item import RequestedItemReviewContextRequestedItem

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemReviewContextRequestedItem from a JSON string
requested_item_review_context_requested_item_instance = RequestedItemReviewContextRequestedItem.from_json(json)
# print the JSON string representation of the object
print(RequestedItemReviewContextRequestedItem.to_json())

# convert the object into a dict
requested_item_review_context_requested_item_dict = requested_item_review_context_requested_item_instance.to_dict()
# create an instance of RequestedItemReviewContextRequestedItem from a dict
requested_item_review_context_requested_item_from_dict = RequestedItemReviewContextRequestedItem.from_dict(requested_item_review_context_requested_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


