# PublishPendingDealRequest

The body of PATCH /deals/{dealId} (WINAD-10699) plus vendor_id; see POST /deals/{dealId}/publish.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal** | [**PublishPendingDealRequestDeal**](PublishPendingDealRequestDeal.md) |  | [optional] 
**deal_detail** | [**PublishPendingDealRequestDealDetail**](PublishPendingDealRequestDealDetail.md) |  | [optional] 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

## Example

```python
from winthrop_client_python.models.publish_pending_deal_request import PublishPendingDealRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPendingDealRequest from a JSON string
publish_pending_deal_request_instance = PublishPendingDealRequest.from_json(json)
# print the JSON string representation of the object
print(PublishPendingDealRequest.to_json())

# convert the object into a dict
publish_pending_deal_request_dict = publish_pending_deal_request_instance.to_dict()
# create an instance of PublishPendingDealRequest from a dict
publish_pending_deal_request_from_dict = PublishPendingDealRequest.from_dict(publish_pending_deal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


