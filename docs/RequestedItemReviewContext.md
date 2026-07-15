# RequestedItemReviewContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_item** | [**RequestedItemReviewContextRequestedItem**](RequestedItemReviewContextRequestedItem.md) |  | 
**ri_note** | **str** | Current note text for the requested item. Always a string; empty string when no note exists. | 
**foia_request** | [**RequestedItemReviewContextFoiaRequest**](RequestedItemReviewContextFoiaRequest.md) |  | 
**existing_document** | [**RequestedItemReviewContextDocument**](RequestedItemReviewContextDocument.md) | Existing document that already represents the requested item. Null when no document exists, when the caller is not authorized to read it, or when more than one candidate document matches. | 

## Example

```python
from winthrop_client_python.models.requested_item_review_context import RequestedItemReviewContext

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemReviewContext from a JSON string
requested_item_review_context_instance = RequestedItemReviewContext.from_json(json)
# print the JSON string representation of the object
print(RequestedItemReviewContext.to_json())

# convert the object into a dict
requested_item_review_context_dict = requested_item_review_context_instance.to_dict()
# create an instance of RequestedItemReviewContext from a dict
requested_item_review_context_from_dict = RequestedItemReviewContext.from_dict(requested_item_review_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


