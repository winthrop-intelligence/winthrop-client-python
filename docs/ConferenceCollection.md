# ConferenceCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Conference]**](Conference.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.conference_collection import ConferenceCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceCollection from a JSON string
conference_collection_instance = ConferenceCollection.from_json(json)
# print the JSON string representation of the object
print ConferenceCollection.to_json()

# convert the object into a dict
conference_collection_dict = conference_collection_instance.to_dict()
# create an instance of ConferenceCollection from a dict
conference_collection_form_dict = conference_collection.from_dict(conference_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


