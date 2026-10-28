# SwapContractRawContractsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_ids** | **List[int]** |  | 
**change_note** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.swap_contract_raw_contracts_request import SwapContractRawContractsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SwapContractRawContractsRequest from a JSON string
swap_contract_raw_contracts_request_instance = SwapContractRawContractsRequest.from_json(json)
# print the JSON string representation of the object
print(SwapContractRawContractsRequest.to_json())

# convert the object into a dict
swap_contract_raw_contracts_request_dict = swap_contract_raw_contracts_request_instance.to_dict()
# create an instance of SwapContractRawContractsRequest from a dict
swap_contract_raw_contracts_request_from_dict = SwapContractRawContractsRequest.from_dict(swap_contract_raw_contracts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


