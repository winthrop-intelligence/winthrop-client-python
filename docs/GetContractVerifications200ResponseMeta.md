# GetContractVerifications200ResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**verified_seasons** | **List[int]** | Seasons whose latest event is passed; a revocation removes a season until re-verified | [optional] 

## Example

```python
from winthrop_client_python.models.get_contract_verifications200_response_meta import GetContractVerifications200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GetContractVerifications200ResponseMeta from a JSON string
get_contract_verifications200_response_meta_instance = GetContractVerifications200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print(GetContractVerifications200ResponseMeta.to_json())

# convert the object into a dict
get_contract_verifications200_response_meta_dict = get_contract_verifications200_response_meta_instance.to_dict()
# create an instance of GetContractVerifications200ResponseMeta from a dict
get_contract_verifications200_response_meta_from_dict = GetContractVerifications200ResponseMeta.from_dict(get_contract_verifications200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


