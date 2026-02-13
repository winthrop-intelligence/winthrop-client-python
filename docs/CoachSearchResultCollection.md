# CoachSearchResultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CoachSearchResult]**](CoachSearchResult.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_search_result_collection import CoachSearchResultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CoachSearchResultCollection from a JSON string
coach_search_result_collection_instance = CoachSearchResultCollection.from_json(json)
# print the JSON string representation of the object
print(CoachSearchResultCollection.to_json())

# convert the object into a dict
coach_search_result_collection_dict = coach_search_result_collection_instance.to_dict()
# create an instance of CoachSearchResultCollection from a dict
coach_search_result_collection_from_dict = CoachSearchResultCollection.from_dict(coach_search_result_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


