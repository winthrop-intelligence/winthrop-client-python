# BulkUpdateAdminContractRequestSearchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_note** | **str** |  | [optional] 
**contract_status_id** | **int** | Nonzero ID of an existing ContractStatus. Positive updates compensation status; negative updates income report status using the absolute ID. Numeric form strings are also accepted; malformed or nonexistent IDs are rejected before any writes. | 
**position_ids** | **List[int]** |  | 

## Example

```python
from winthrop_client_python.models.bulk_update_admin_contract_request_searches_request import BulkUpdateAdminContractRequestSearchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateAdminContractRequestSearchesRequest from a JSON string
bulk_update_admin_contract_request_searches_request_instance = BulkUpdateAdminContractRequestSearchesRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateAdminContractRequestSearchesRequest.to_json())

# convert the object into a dict
bulk_update_admin_contract_request_searches_request_dict = bulk_update_admin_contract_request_searches_request_instance.to_dict()
# create an instance of BulkUpdateAdminContractRequestSearchesRequest from a dict
bulk_update_admin_contract_request_searches_request_from_dict = BulkUpdateAdminContractRequestSearchesRequest.from_dict(bulk_update_admin_contract_request_searches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


