# PublishedContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**executed_on** | **date** |  | [optional] 
**expires_on** | **date** |  | [optional] 
**start_on** | **date** |  | [optional] 
**end_on** | **date** |  | [optional] 
**at_will** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**pending** | **bool** | Pending contracts are undated PDFs awaiting entry. They skip the date validations, cannot be linked to a compensation, and are hidden from customers. Filter with q[pending_eq]&#x3D;true. | [optional] 
**contractable_type** | **str** |  | [optional] 
**contractable_id** | **int** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**compensation_ids** | **List[int]** | The compensations written, oldest year first within each school | [optional] 
**compensations** | [**List[PublishedContractAllOfCompensations]**](PublishedContractAllOfCompensations.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.published_contract import PublishedContract

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedContract from a JSON string
published_contract_instance = PublishedContract.from_json(json)
# print the JSON string representation of the object
print(PublishedContract.to_json())

# convert the object into a dict
published_contract_dict = published_contract_instance.to_dict()
# create an instance of PublishedContract from a dict
published_contract_from_dict = PublishedContract.from_dict(published_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


