# SeasonCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Season]**](Season.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.season_collection import SeasonCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonCollection from a JSON string
season_collection_instance = SeasonCollection.from_json(json)
# print the JSON string representation of the object
print(SeasonCollection.to_json())

# convert the object into a dict
season_collection_dict = season_collection_instance.to_dict()
# create an instance of SeasonCollection from a dict
season_collection_form_dict = season_collection.from_dict(season_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


