# UpdateDealRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal** | [**UpdateDealRequestDeal**](UpdateDealRequestDeal.md) |  | [optional] 
**deal_detail** | [**UpdateDealRequestDealDetail**](UpdateDealRequestDealDetail.md) |  | [optional] 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

## Example

```python
from winthrop_client_python.models.update_deal_request import UpdateDealRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDealRequest from a JSON string
update_deal_request_instance = UpdateDealRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDealRequest.to_json())

# convert the object into a dict
update_deal_request_dict = update_deal_request_instance.to_dict()
# create an instance of UpdateDealRequest from a dict
update_deal_request_from_dict = UpdateDealRequest.from_dict(update_deal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


