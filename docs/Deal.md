# Deal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**vendor_id** | **int** |  | [optional] 
**start_at** | **datetime** |  | [optional] 
**end_at** | **datetime** |  | [optional] 
**signed** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**text** | **str** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**deal_type_id** | **int** |  | [optional] 
**archived** | **bool** |  | [optional] 
**deal_status_type_id** | **int** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.deal import Deal

# TODO update the JSON string below
json = "{}"
# create an instance of Deal from a JSON string
deal_instance = Deal.from_json(json)
# print the JSON string representation of the object
print(Deal.to_json())

# convert the object into a dict
deal_dict = deal_instance.to_dict()
# create an instance of Deal from a dict
deal_from_dict = Deal.from_dict(deal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


