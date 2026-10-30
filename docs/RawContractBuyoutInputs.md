# RawContractBuyoutInputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the RawContract | 
**buyout_inputs** | [**BuyoutInputs**](BuyoutInputs.md) |  | 
**buyout_inputs_updated_at** | **datetime** |  | 
**buyout_inputs_stale** | **bool** | True when, after the newest revision, the contract&#39;s OCR text was redone or its contract_terms changed. The inputs are kept; re-check and store them again to clear it. | 
**buyout_inputs_stale_reasons** | **List[str]** |  | 

## Example

```python
from winthrop_client_python.models.raw_contract_buyout_inputs import RawContractBuyoutInputs

# TODO update the JSON string below
json = "{}"
# create an instance of RawContractBuyoutInputs from a JSON string
raw_contract_buyout_inputs_instance = RawContractBuyoutInputs.from_json(json)
# print the JSON string representation of the object
print(RawContractBuyoutInputs.to_json())

# convert the object into a dict
raw_contract_buyout_inputs_dict = raw_contract_buyout_inputs_instance.to_dict()
# create an instance of RawContractBuyoutInputs from a dict
raw_contract_buyout_inputs_from_dict = RawContractBuyoutInputs.from_dict(raw_contract_buyout_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


