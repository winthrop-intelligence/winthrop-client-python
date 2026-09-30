# PendingContractCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The new contract&#39;s id | 
**raw_contract_id** | **int** | The id of the RawContract holding the PDF | 
**filename** | **str** | The uploaded PDF&#39;s filename | 
**coach_id** | **int** |  | 
**pending** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.pending_contract_created import PendingContractCreated

# TODO update the JSON string below
json = "{}"
# create an instance of PendingContractCreated from a JSON string
pending_contract_created_instance = PendingContractCreated.from_json(json)
# print the JSON string representation of the object
print(PendingContractCreated.to_json())

# convert the object into a dict
pending_contract_created_dict = pending_contract_created_instance.to_dict()
# create an instance of PendingContractCreated from a dict
pending_contract_created_from_dict = PendingContractCreated.from_dict(pending_contract_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


