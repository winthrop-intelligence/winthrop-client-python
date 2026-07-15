# RequestedItemReviewContextDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Raw contract (document) ID for duplicate and review checks. | 
**label** | **str** | Canonical WinAD document label. | 
**has_file** | **bool** | True when the document has a non-empty attached file. | 
**file_name** | **str** | Attached file name; null when has_file is false. | 
**content_type** | **str** |  | 
**byte_size** | **int** | Attached file size in bytes; null when has_file is false. | 

## Example

```python
from winthrop_client_python.models.requested_item_review_context_document import RequestedItemReviewContextDocument

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemReviewContextDocument from a JSON string
requested_item_review_context_document_instance = RequestedItemReviewContextDocument.from_json(json)
# print the JSON string representation of the object
print(RequestedItemReviewContextDocument.to_json())

# convert the object into a dict
requested_item_review_context_document_dict = requested_item_review_context_document_instance.to_dict()
# create an instance of RequestedItemReviewContextDocument from a dict
requested_item_review_context_document_from_dict = RequestedItemReviewContextDocument.from_dict(requested_item_review_context_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


