# GetDealVerifications200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**GetDealVerifications200ResponseMeta**](GetDealVerifications200ResponseMeta.md) |  | 
**data** | [**List[DealVerification]**](DealVerification.md) |  | 

## Example

```python
from winthrop_client_python.models.get_deal_verifications200_response import GetDealVerifications200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDealVerifications200Response from a JSON string
get_deal_verifications200_response_instance = GetDealVerifications200Response.from_json(json)
# print the JSON string representation of the object
print(GetDealVerifications200Response.to_json())

# convert the object into a dict
get_deal_verifications200_response_dict = get_deal_verifications200_response_instance.to_dict()
# create an instance of GetDealVerifications200Response from a dict
get_deal_verifications200_response_from_dict = GetDealVerifications200Response.from_dict(get_deal_verifications200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


