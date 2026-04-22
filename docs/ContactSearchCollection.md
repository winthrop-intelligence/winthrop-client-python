# ContactSearchCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ContactSearchEntry]**](ContactSearchEntry.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.contact_search_collection import ContactSearchCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ContactSearchCollection from a JSON string
contact_search_collection_instance = ContactSearchCollection.from_json(json)
# print the JSON string representation of the object
print(ContactSearchCollection.to_json())

# convert the object into a dict
contact_search_collection_dict = contact_search_collection_instance.to_dict()
# create an instance of ContactSearchCollection from a dict
contact_search_collection_from_dict = ContactSearchCollection.from_dict(contact_search_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


