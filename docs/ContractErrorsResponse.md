# ContractErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_compensation_ids** | **List[int]** | Only on a refused coach move (PATCH /contracts/{contractId}). The compensations that still link to the contract. | [optional] 
**linked_position_ids** | **List[int]** | Only on a refused coach move. The positions of those compensations. | [optional] 
**linked_verification_ids** | **List[int]** | Only on a refused coach move. The verification events recorded for the contract. | [optional] 
**linked_earned_incentive_ids** | **List[int]** | Only on a refused coach move. The earned incentives whose raw_contract_id or ended_by_contract_id is the contract&#39;s RawContract, in id order, each once. | [optional] 
**code** | **str** | Only on a refused Drive-source upload (POST /contracts with source_drive_file_id, WINAD-10673). Stable machine-readable reason; source_timeout and source_error are answered with 503 and may be retried unchanged. | [optional] 
**errors** | **Dict[str, List[str]]** | Error messages keyed by attribute (base for whole-request errors) | 

## Example

```python
from winthrop_client_python.models.contract_errors_response import ContractErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractErrorsResponse from a JSON string
contract_errors_response_instance = ContractErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(ContractErrorsResponse.to_json())

# convert the object into a dict
contract_errors_response_dict = contract_errors_response_instance.to_dict()
# create an instance of ContractErrorsResponse from a dict
contract_errors_response_from_dict = ContractErrorsResponse.from_dict(contract_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


