# EadaFinancialSearchResultRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**school_name** | **str** |  | [optional] 
**year** | **int** |  | 
**match_status** | **str** |  | [optional] 
**sport_code** | **str** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**mapping_status** | **str** |  | [optional] 
**metrics** | [**List[EadaNormalizedMetric]**](EadaNormalizedMetric.md) |  | 
**source_payload** | **object** |  | [optional] 

## Example

```python
from winthrop_client_python.models.eada_financial_search_result_row import EadaFinancialSearchResultRow

# TODO update the JSON string below
json = "{}"
# create an instance of EadaFinancialSearchResultRow from a JSON string
eada_financial_search_result_row_instance = EadaFinancialSearchResultRow.from_json(json)
# print the JSON string representation of the object
print(EadaFinancialSearchResultRow.to_json())

# convert the object into a dict
eada_financial_search_result_row_dict = eada_financial_search_result_row_instance.to_dict()
# create an instance of EadaFinancialSearchResultRow from a dict
eada_financial_search_result_row_from_dict = EadaFinancialSearchResultRow.from_dict(eada_financial_search_result_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


