# PublishPendingDealRequestDeal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **int** | An existing vendor. Replaces the vendor the upload attached. Required unless the deal already has a vendor. | [optional] 
**start_on** | **date** | Optional plain calendar date, strictly YYYY-MM-DD and a real date (422 deal.start_on otherwise); null leaves the start empty. Stored as midnight UTC. Cannot be sent together with start_at. | [optional] 
**end_on** | **date** | Required (here or already on the deal): the last day of the deal, a plain calendar date as start_on; null is refused. Cannot be sent together with end_at. | [optional] 
**start_at** | **date** | The same as start_on (a plain YYYY-MM-DD date, not a datetime). Cannot be sent together with start_on. | [optional] 
**end_at** | **date** | The same as end_on (a plain YYYY-MM-DD date, not a datetime; null is refused). Cannot be sent together with end_on. | [optional] 
**autorenew** | **bool** |  | [optional] 
**text** | **str** | WINAD-10738. The deal&#39;s summary, plain text; blank or null leaves it empty. | [optional] 
**vendor_ids** | **List[int]** | WINAD-10738. Existing vendors, as in PATCH. Cannot be sent together with vendor_id. | [optional] 
**school_id** | **int** | WINAD-10738. An existing school, as in PATCH. | [optional] 

## Example

```python
from winthrop_client_python.models.publish_pending_deal_request_deal import PublishPendingDealRequestDeal

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPendingDealRequestDeal from a JSON string
publish_pending_deal_request_deal_instance = PublishPendingDealRequestDeal.from_json(json)
# print the JSON string representation of the object
print(PublishPendingDealRequestDeal.to_json())

# convert the object into a dict
publish_pending_deal_request_deal_dict = publish_pending_deal_request_deal_instance.to_dict()
# create an instance of PublishPendingDealRequestDeal from a dict
publish_pending_deal_request_deal_from_dict = PublishPendingDealRequestDeal.from_dict(publish_pending_deal_request_deal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


