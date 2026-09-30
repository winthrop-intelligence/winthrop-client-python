# CreateContractVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_verification** | [**ContractVerificationInput**](ContractVerificationInput.md) |  | 

## Example

```python
from winthrop_client_python.models.create_contract_verification_request import CreateContractVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractVerificationRequest from a JSON string
create_contract_verification_request_instance = CreateContractVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateContractVerificationRequest.to_json())

# convert the object into a dict
create_contract_verification_request_dict = create_contract_verification_request_instance.to_dict()
# create an instance of CreateContractVerificationRequest from a dict
create_contract_verification_request_from_dict = CreateContractVerificationRequest.from_dict(create_contract_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


