# MultimediaDealUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grf** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**bha** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**signing_bonus** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**additional_rev** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**rev_share_percent** | [**MultimediaDealUpdateRevSharePercent**](MultimediaDealUpdateRevSharePercent.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.multimedia_deal_update import MultimediaDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MultimediaDealUpdate from a JSON string
multimedia_deal_update_instance = MultimediaDealUpdate.from_json(json)
# print the JSON string representation of the object
print(MultimediaDealUpdate.to_json())

# convert the object into a dict
multimedia_deal_update_dict = multimedia_deal_update_instance.to_dict()
# create an instance of MultimediaDealUpdate from a dict
multimedia_deal_update_from_dict = MultimediaDealUpdate.from_dict(multimedia_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


