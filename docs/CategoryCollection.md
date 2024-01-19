# CategoryCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Category]**](Category.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.category_collection import CategoryCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryCollection from a JSON string
category_collection_instance = CategoryCollection.from_json(json)
# print the JSON string representation of the object
print CategoryCollection.to_json()

# convert the object into a dict
category_collection_dict = category_collection_instance.to_dict()
# create an instance of CategoryCollection from a dict
category_collection_form_dict = category_collection.from_dict(category_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


