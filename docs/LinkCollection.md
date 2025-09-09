# LinkCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.link_collection import LinkCollection

# TODO update the JSON string below
json = "{}"
# create an instance of LinkCollection from a JSON string
link_collection_instance = LinkCollection.from_json(json)
# print the JSON string representation of the object
print(LinkCollection.to_json())

# convert the object into a dict
link_collection_dict = link_collection_instance.to_dict()
# create an instance of LinkCollection from a dict
link_collection_from_dict = LinkCollection.from_dict(link_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


