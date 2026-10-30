# DealDetailPosition

The position being filled (Executive Search only), with its title and the person holding it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**person** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.deal_detail_position import DealDetailPosition

# TODO update the JSON string below
json = "{}"
# create an instance of DealDetailPosition from a JSON string
deal_detail_position_instance = DealDetailPosition.from_json(json)
# print the JSON string representation of the object
print(DealDetailPosition.to_json())

# convert the object into a dict
deal_detail_position_dict = deal_detail_position_instance.to_dict()
# create an instance of DealDetailPosition from a dict
deal_detail_position_from_dict = DealDetailPosition.from_dict(deal_detail_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


