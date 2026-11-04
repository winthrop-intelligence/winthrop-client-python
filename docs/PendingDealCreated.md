# PendingDealCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The new deal&#39;s id | 
**raw_contract_id** | **int** | The id of the vendor RawContract holding the PDF | 
**filename** | **str** | The uploaded PDF&#39;s filename | 
**school_id** | **int** |  | 
**deal_type** | **str** | The deal type&#39;s display name, for example Apparel | 
**pending** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.pending_deal_created import PendingDealCreated

# TODO update the JSON string below
json = "{}"
# create an instance of PendingDealCreated from a JSON string
pending_deal_created_instance = PendingDealCreated.from_json(json)
# print the JSON string representation of the object
print(PendingDealCreated.to_json())

# convert the object into a dict
pending_deal_created_dict = pending_deal_created_instance.to_dict()
# create an instance of PendingDealCreated from a dict
pending_deal_created_from_dict = PendingDealCreated.from_dict(pending_deal_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


