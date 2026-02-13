# GadSearchResultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GadSearchResult]**](GadSearchResult.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**stats** | [**GadSearchStats**](GadSearchStats.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.gad_search_result_collection import GadSearchResultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GadSearchResultCollection from a JSON string
gad_search_result_collection_instance = GadSearchResultCollection.from_json(json)
# print the JSON string representation of the object
print(GadSearchResultCollection.to_json())

# convert the object into a dict
gad_search_result_collection_dict = gad_search_result_collection_instance.to_dict()
# create an instance of GadSearchResultCollection from a dict
gad_search_result_collection_from_dict = GadSearchResultCollection.from_dict(gad_search_result_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


