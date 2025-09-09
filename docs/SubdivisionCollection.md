# SubdivisionCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Subdivision]**](Subdivision.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.subdivision_collection import SubdivisionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SubdivisionCollection from a JSON string
subdivision_collection_instance = SubdivisionCollection.from_json(json)
# print the JSON string representation of the object
print(SubdivisionCollection.to_json())

# convert the object into a dict
subdivision_collection_dict = subdivision_collection_instance.to_dict()
# create an instance of SubdivisionCollection from a dict
subdivision_collection_from_dict = SubdivisionCollection.from_dict(subdivision_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


