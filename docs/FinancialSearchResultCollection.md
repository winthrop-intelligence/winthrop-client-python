# FinancialSearchResultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FinancialSearchResult]**](FinancialSearchResult.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.financial_search_result_collection import FinancialSearchResultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialSearchResultCollection from a JSON string
financial_search_result_collection_instance = FinancialSearchResultCollection.from_json(json)
# print the JSON string representation of the object
print(FinancialSearchResultCollection.to_json())

# convert the object into a dict
financial_search_result_collection_dict = financial_search_result_collection_instance.to_dict()
# create an instance of FinancialSearchResultCollection from a dict
financial_search_result_collection_from_dict = FinancialSearchResultCollection.from_dict(financial_search_result_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


