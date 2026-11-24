# PendingGameContractErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Stable reason of a refused upload (invalid_input, invalid_pdf, checksum_mismatch, duplicate, ...). | [optional] 
**errors** | **Dict[str, List[str]]** | Attribute (school_id, foia_label_id, file, drive_id, expected_sha256, base) mapped to its messages. | 

## Example

```python
from winthrop_client_python.models.pending_game_contract_errors_response import PendingGameContractErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PendingGameContractErrorsResponse from a JSON string
pending_game_contract_errors_response_instance = PendingGameContractErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(PendingGameContractErrorsResponse.to_json())

# convert the object into a dict
pending_game_contract_errors_response_dict = pending_game_contract_errors_response_instance.to_dict()
# create an instance of PendingGameContractErrorsResponse from a dict
pending_game_contract_errors_response_from_dict = PendingGameContractErrorsResponse.from_dict(pending_game_contract_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


