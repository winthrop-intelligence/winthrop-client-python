# CreatePendingContract201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**raw_contract_id** | **int** |  | 
**filename** | **str** | The uploaded PDF&#39;s filename | 
**coach_id** | **int** |  | 
**pending** | **bool** | Pending contracts are undated PDFs awaiting entry. They skip the date validations, cannot be linked to a compensation, and are hidden from customers. Filter with q[pending_eq]&#x3D;true. | 
**executed_on** | **date** |  | [optional] 
**expires_on** | **date** |  | [optional] 
**contingent_change** | **bool** |  | [optional] 
**start_on** | **date** |  | [optional] 
**end_on** | **date** |  | [optional] 
**at_will** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**contractable_type** | **str** |  | [optional] 
**contractable_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_pending_contract201_response import CreatePendingContract201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePendingContract201Response from a JSON string
create_pending_contract201_response_instance = CreatePendingContract201Response.from_json(json)
# print the JSON string representation of the object
print(CreatePendingContract201Response.to_json())

# convert the object into a dict
create_pending_contract201_response_dict = create_pending_contract201_response_instance.to_dict()
# create an instance of CreatePendingContract201Response from a dict
create_pending_contract201_response_from_dict = CreatePendingContract201Response.from_dict(create_pending_contract201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


