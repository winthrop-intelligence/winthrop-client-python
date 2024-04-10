# DealStatusCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DealStatus]**](DealStatus.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.deal_status_collection import DealStatusCollection

# TODO update the JSON string below
json = "{}"
# create an instance of DealStatusCollection from a JSON string
deal_status_collection_instance = DealStatusCollection.from_json(json)
# print the JSON string representation of the object
print(DealStatusCollection.to_json())

# convert the object into a dict
deal_status_collection_dict = deal_status_collection_instance.to_dict()
# create an instance of DealStatusCollection from a dict
deal_status_collection_form_dict = deal_status_collection.from_dict(deal_status_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


