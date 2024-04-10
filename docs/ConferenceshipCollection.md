# ConferenceshipCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Conferenceship]**](Conferenceship.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.conferenceship_collection import ConferenceshipCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceshipCollection from a JSON string
conferenceship_collection_instance = ConferenceshipCollection.from_json(json)
# print the JSON string representation of the object
print ConferenceshipCollection.to_json()

# convert the object into a dict
conferenceship_collection_dict = conferenceship_collection_instance.to_dict()
# create an instance of ConferenceshipCollection from a dict
conferenceship_collection_form_dict = conferenceship_collection.from_dict(conferenceship_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


