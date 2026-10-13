# PublishPendingContractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 
**start_on** | **date** | Contract start date (YYYY-MM-DD) | 
**end_on** | **date** | Contract end date (YYYY-MM-DD). Required unless at_will is true, and must be blank when it is. | [optional] 
**at_will** | **bool** | Sent explicitly (the CSV infers it from a blank end date) | 
**executed_on** | **date** | Optional date the contract was executed (YYYY-MM-DD) | [optional] 
**expires_on** | **date** | Optional date the contract expires (YYYY-MM-DD) | [optional] 
**contingent_change** | **bool** | Optional. Whether the terms are contingent on a change; left out (or null or empty, like the other optional fields of publish), the stored value (false for a new contract) stays. Anything but true or false is refused. | [optional] 
**compensations** | [**List[PublishPendingContractCompensation]**](PublishPendingContractCompensation.md) | One entry per school and year | 
**contract_terms** | [**PublishPendingContractRequestContractTerms**](PublishPendingContractRequestContractTerms.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.publish_pending_contract_request import PublishPendingContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPendingContractRequest from a JSON string
publish_pending_contract_request_instance = PublishPendingContractRequest.from_json(json)
# print the JSON string representation of the object
print(PublishPendingContractRequest.to_json())

# convert the object into a dict
publish_pending_contract_request_dict = publish_pending_contract_request_instance.to_dict()
# create an instance of PublishPendingContractRequest from a dict
publish_pending_contract_request_from_dict = PublishPendingContractRequest.from_dict(publish_pending_contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


