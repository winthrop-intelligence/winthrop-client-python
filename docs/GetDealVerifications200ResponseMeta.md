# GetDealVerifications200ResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**verified** | **bool** | True while the latest event is passed; a later mismatch, could_not_verify or revocation withdraws it | [optional] 

## Example

```python
from winthrop_client_python.models.get_deal_verifications200_response_meta import GetDealVerifications200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GetDealVerifications200ResponseMeta from a JSON string
get_deal_verifications200_response_meta_instance = GetDealVerifications200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print(GetDealVerifications200ResponseMeta.to_json())

# convert the object into a dict
get_deal_verifications200_response_meta_dict = get_deal_verifications200_response_meta_instance.to_dict()
# create an instance of GetDealVerifications200ResponseMeta from a dict
get_deal_verifications200_response_meta_from_dict = GetDealVerifications200ResponseMeta.from_dict(get_deal_verifications200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


