# DealStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | 
**auto_renew** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**source_note** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**deal_status_type_id** | **int** |  | [optional] 
**deal_type_id** | **int** |  | 

## Example

```python
from winthrop_client_python.models.deal_status import DealStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DealStatus from a JSON string
deal_status_instance = DealStatus.from_json(json)
# print the JSON string representation of the object
print DealStatus.to_json()

# convert the object into a dict
deal_status_dict = deal_status_instance.to_dict()
# create an instance of DealStatus from a dict
deal_status_form_dict = deal_status.from_dict(deal_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


