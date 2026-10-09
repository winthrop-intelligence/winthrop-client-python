# UpdateContractRequest

Partial update of a published contract. At least one of start_on, end_on or at_will is required; change_note alone is insufficient. Pending contracts are published, not edited. Setting at_will true requires end_on null. Changes are audited with the authenticated user and the optional change_note. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_on** | **date** | Contract start date (strict YYYY-MM-DD); cannot be null. | [optional] 
**end_on** | **date** | Contract end date (strict YYYY-MM-DD). Must be null or omitted when at_will is true; an existing end date must explicitly be cleared. Required in the resulting record unless at_will is true. | [optional] 
**at_will** | **bool** | Whether employment is at will; only JSON true or false is accepted. | [optional] 
**change_note** | **str** | Why this change is being made, for the internal audit history (WINAD-10632). It is stored on the audit version this write creates and is never returned. Blank is the same as omitted; a non-string value is refused with 422 (errors.change_note). It is not an updatable field: a request with only a change_note is refused. | [optional] 

## Example

```python
from winthrop_client_python.models.update_contract_request import UpdateContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContractRequest from a JSON string
update_contract_request_instance = UpdateContractRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateContractRequest.to_json())

# convert the object into a dict
update_contract_request_dict = update_contract_request_instance.to_dict()
# create an instance of UpdateContractRequest from a dict
update_contract_request_from_dict = UpdateContractRequest.from_dict(update_contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


