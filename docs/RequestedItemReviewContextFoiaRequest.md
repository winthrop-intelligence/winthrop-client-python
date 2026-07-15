# RequestedItemReviewContextFoiaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**label** | **str** | Name of the FOIA label attached to the FOIA request. | 
**admin_url** | **str** | Environment-aware legacy admin URL for the parent FOIA request, ending with /old/admin/foia_requests/{foiaRequestId}#requested_item_{requestedItemId}. | 

## Example

```python
from winthrop_client_python.models.requested_item_review_context_foia_request import RequestedItemReviewContextFoiaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemReviewContextFoiaRequest from a JSON string
requested_item_review_context_foia_request_instance = RequestedItemReviewContextFoiaRequest.from_json(json)
# print the JSON string representation of the object
print(RequestedItemReviewContextFoiaRequest.to_json())

# convert the object into a dict
requested_item_review_context_foia_request_dict = requested_item_review_context_foia_request_instance.to_dict()
# create an instance of RequestedItemReviewContextFoiaRequest from a dict
requested_item_review_context_foia_request_from_dict = RequestedItemReviewContextFoiaRequest.from_dict(requested_item_review_context_foia_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


