# SchoolCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[School]**](School.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_collection import SchoolCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolCollection from a JSON string
school_collection_instance = SchoolCollection.from_json(json)
# print the JSON string representation of the object
print(SchoolCollection.to_json())

# convert the object into a dict
school_collection_dict = school_collection_instance.to_dict()
# create an instance of SchoolCollection from a dict
school_collection_from_dict = SchoolCollection.from_dict(school_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


