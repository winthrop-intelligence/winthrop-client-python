# RawContractBuyoutInputRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**raw_contract_id** | **int** |  | 
**user_id** | **int** |  | 
**change_note** | **str** |  | 
**created_at** | **datetime** |  | 
**document** | [**BuyoutInputs**](BuyoutInputs.md) |  | 

## Example

```python
from winthrop_client_python.models.raw_contract_buyout_input_revision import RawContractBuyoutInputRevision

# TODO update the JSON string below
json = "{}"
# create an instance of RawContractBuyoutInputRevision from a JSON string
raw_contract_buyout_input_revision_instance = RawContractBuyoutInputRevision.from_json(json)
# print the JSON string representation of the object
print(RawContractBuyoutInputRevision.to_json())

# convert the object into a dict
raw_contract_buyout_input_revision_dict = raw_contract_buyout_input_revision_instance.to_dict()
# create an instance of RawContractBuyoutInputRevision from a dict
raw_contract_buyout_input_revision_from_dict = RawContractBuyoutInputRevision.from_dict(raw_contract_buyout_input_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


