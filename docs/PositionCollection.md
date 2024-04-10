# PositionCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Position]**](Position.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.position_collection import PositionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of PositionCollection from a JSON string
position_collection_instance = PositionCollection.from_json(json)
# print the JSON string representation of the object
print(PositionCollection.to_json())

# convert the object into a dict
position_collection_dict = position_collection_instance.to_dict()
# create an instance of PositionCollection from a dict
position_collection_form_dict = position_collection.from_dict(position_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


