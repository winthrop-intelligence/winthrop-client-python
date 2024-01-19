# SportCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Sport]**](Sport.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.sport_collection import SportCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SportCollection from a JSON string
sport_collection_instance = SportCollection.from_json(json)
# print the JSON string representation of the object
print SportCollection.to_json()

# convert the object into a dict
sport_collection_dict = sport_collection_instance.to_dict()
# create an instance of SportCollection from a dict
sport_collection_form_dict = sport_collection.from_dict(sport_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


