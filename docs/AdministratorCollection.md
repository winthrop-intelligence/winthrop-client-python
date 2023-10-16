# AdministratorCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Administrator]**](Administrator.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.administrator_collection import AdministratorCollection

# TODO update the JSON string below
json = "{}"
# create an instance of AdministratorCollection from a JSON string
administrator_collection_instance = AdministratorCollection.from_json(json)
# print the JSON string representation of the object
print AdministratorCollection.to_json()

# convert the object into a dict
administrator_collection_dict = administrator_collection_instance.to_dict()
# create an instance of AdministratorCollection from a dict
administrator_collection_form_dict = administrator_collection.from_dict(administrator_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


