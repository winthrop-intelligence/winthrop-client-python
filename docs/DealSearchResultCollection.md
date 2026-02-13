# DealSearchResultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DealSearchResult]**](DealSearchResult.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.deal_search_result_collection import DealSearchResultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of DealSearchResultCollection from a JSON string
deal_search_result_collection_instance = DealSearchResultCollection.from_json(json)
# print the JSON string representation of the object
print(DealSearchResultCollection.to_json())

# convert the object into a dict
deal_search_result_collection_dict = deal_search_result_collection_instance.to_dict()
# create an instance of DealSearchResultCollection from a dict
deal_search_result_collection_from_dict = DealSearchResultCollection.from_dict(deal_search_result_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


