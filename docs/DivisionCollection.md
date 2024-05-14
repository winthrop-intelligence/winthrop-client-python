# DivisionCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Division]**](Division.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.division_collection import DivisionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of DivisionCollection from a JSON string
division_collection_instance = DivisionCollection.from_json(json)
# print the JSON string representation of the object
print(DivisionCollection.to_json())

# convert the object into a dict
division_collection_dict = division_collection_instance.to_dict()
# create an instance of DivisionCollection from a dict
division_collection_form_dict = division_collection.from_dict(division_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


