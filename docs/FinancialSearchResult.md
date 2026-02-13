# FinancialSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**division_id** | **int** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**total_student_enrollment** | **int** |  | [optional] 
**student_athlete_enrollment** | **int** |  | [optional] 
**sport_count** | **int** |  | [optional] 
**rev_total_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_ticket_sales_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_contributions_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_rights_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_student_fees_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_university_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_guarantees_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_total_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_coaching_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_recruiting_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_travel_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_facilities_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_guarantees_amt** | **float** | Amount in whole US dollars | [optional] 

## Example

```python
from winthrop_client_python.models.financial_search_result import FinancialSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialSearchResult from a JSON string
financial_search_result_instance = FinancialSearchResult.from_json(json)
# print the JSON string representation of the object
print(FinancialSearchResult.to_json())

# convert the object into a dict
financial_search_result_dict = financial_search_result_instance.to_dict()
# create an instance of FinancialSearchResult from a dict
financial_search_result_from_dict = FinancialSearchResult.from_dict(financial_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


