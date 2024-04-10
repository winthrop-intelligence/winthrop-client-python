# RequestedItemCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RequestedItem]**](RequestedItem.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.requested_item_collection import RequestedItemCollection

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemCollection from a JSON string
requested_item_collection_instance = RequestedItemCollection.from_json(json)
# print the JSON string representation of the object
print(RequestedItemCollection.to_json())

# convert the object into a dict
requested_item_collection_dict = requested_item_collection_instance.to_dict()
# create an instance of RequestedItemCollection from a dict
requested_item_collection_form_dict = requested_item_collection.from_dict(requested_item_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


