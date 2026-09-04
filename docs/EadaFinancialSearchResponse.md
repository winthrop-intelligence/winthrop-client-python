# EadaFinancialSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**grain** | **str** |  | 
**year** | **int** |  | 
**data** | [**List[EadaFinancialSearchResultRow]**](EadaFinancialSearchResultRow.md) |  | 

## Example

```python
from winthrop_client_python.models.eada_financial_search_response import EadaFinancialSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EadaFinancialSearchResponse from a JSON string
eada_financial_search_response_instance = EadaFinancialSearchResponse.from_json(json)
# print the JSON string representation of the object
print(EadaFinancialSearchResponse.to_json())

# convert the object into a dict
eada_financial_search_response_dict = eada_financial_search_response_instance.to_dict()
# create an instance of EadaFinancialSearchResponse from a dict
eada_financial_search_response_from_dict = EadaFinancialSearchResponse.from_dict(eada_financial_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


