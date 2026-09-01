# PositionTypeCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PositionType]**](PositionType.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.position_type_collection import PositionTypeCollection

# TODO update the JSON string below
json = "{}"
# create an instance of PositionTypeCollection from a JSON string
position_type_collection_instance = PositionTypeCollection.from_json(json)
# print the JSON string representation of the object
print(PositionTypeCollection.to_json())

# convert the object into a dict
position_type_collection_dict = position_type_collection_instance.to_dict()
# create an instance of PositionTypeCollection from a dict
position_type_collection_from_dict = PositionTypeCollection.from_dict(position_type_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


