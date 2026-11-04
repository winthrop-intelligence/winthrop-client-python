# SwapContractRawContracts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contracts** | [**List[SwapContractRawContracts200ResponseContractsInner]**](SwapContractRawContracts200ResponseContractsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.swap_contract_raw_contracts200_response import SwapContractRawContracts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SwapContractRawContracts200Response from a JSON string
swap_contract_raw_contracts200_response_instance = SwapContractRawContracts200Response.from_json(json)
# print the JSON string representation of the object
print(SwapContractRawContracts200Response.to_json())

# convert the object into a dict
swap_contract_raw_contracts200_response_dict = swap_contract_raw_contracts200_response_instance.to_dict()
# create an instance of SwapContractRawContracts200Response from a dict
swap_contract_raw_contracts200_response_from_dict = SwapContractRawContracts200Response.from_dict(swap_contract_raw_contracts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


