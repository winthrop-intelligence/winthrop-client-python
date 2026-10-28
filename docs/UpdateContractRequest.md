# UpdateContractRequest

Partial update of a published contract. At least one of the contract fields is required; change_note alone is insufficient. Pending contracts are published, not edited. Setting at_will true requires end_on null. Changes are audited with the authenticated user and the optional change_note. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_contract_id** | **int** | Id of the RawContract (a coach contract document nobody else holds) the contract should hold from now on. See the PATCH description. | [optional] 
**start_on** | **date** | Contract start date (strict YYYY-MM-DD); cannot be null. | [optional] 
**end_on** | **date** | Contract end date (strict YYYY-MM-DD). Must be null or omitted when at_will is true; an existing end date must explicitly be cleared. Required in the resulting record unless at_will is true. | [optional] 
**at_will** | **bool** | Whether employment is at will; only JSON true or false is accepted. | [optional] 
**executed_on** | **date** | Date the contract was executed (strict YYYY-MM-DD); null clears it. | [optional] 
**expires_on** | **date** | Date the contract expires (strict YYYY-MM-DD); null clears it. | [optional] 
**contingent_change** | **bool** | Whether the terms are contingent on a change; only JSON true or false is accepted. | [optional] 
**coach_id** | **int** | Moves the contract to this coach. Refused (422 errors.coach_id plus linked_compensation_ids, linked_position_ids, linked_verification_ids and linked_earned_incentive_ids) while any of those rows still link to the contract; the agent never relinks them itself. | [optional] 
**contractable_id** | **int** | Same as coach_id (WINAD-10739). Giving both with different values is a 422. | [optional] 
**contractable_type** | **str** | Sets the owner type (WINAD-10739), for example to repair a contract saved with a contractable_id and no type. Only Coach is accepted. A contract with no owner id needs coach_id / contractable_id in the same request, because the type alone is a 422 (errors.contractable_id). Together with coach_id / contractable_id these are the only fields a pending contract accepts. | [optional] 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

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


