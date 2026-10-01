# PublishPendingContractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_on** | **date** | Contract start date (YYYY-MM-DD) | 
**end_on** | **date** | Contract end date (YYYY-MM-DD). Required unless at_will is true, and must be blank when it is. | [optional] 
**at_will** | **bool** | Sent explicitly (the CSV infers it from a blank end date) | 
**executed_on** | **date** | Optional date the contract was executed (YYYY-MM-DD) | [optional] 
**compensations** | [**List[PublishPendingContractCompensation]**](PublishPendingContractCompensation.md) | One entry per school and year | 

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


