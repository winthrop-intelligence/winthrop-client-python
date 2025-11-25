# DealCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Deal]**](Deal.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.deal_collection import DealCollection

# TODO update the JSON string below
json = "{}"
# create an instance of DealCollection from a JSON string
deal_collection_instance = DealCollection.from_json(json)
# print the JSON string representation of the object
print(DealCollection.to_json())

# convert the object into a dict
deal_collection_dict = deal_collection_instance.to_dict()
# create an instance of DealCollection from a dict
deal_collection_from_dict = DealCollection.from_dict(deal_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


