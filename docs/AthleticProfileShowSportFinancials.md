# AthleticProfileShowSportFinancials

Financials tab payload for a sport scope; null for ADMIN scope. Missing or hidden values are null, never zero.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**available_fiscal_years** | **List[int]** | Window fiscal years the school has any financial data for (own FRS sport/institution filings for publics, matched EADA sport/institution reports), oldest first; drives the FY stepper. Empty when every source is missing. | [optional] 
**quadrant** | [**AthleticProfileShowSportFinancialsQuadrant**](AthleticProfileShowSportFinancialsQuadrant.md) |  | [optional] 
**frs_split** | [**AthleticProfileShowSportFinancialsFrsSplit**](AthleticProfileShowSportFinancialsFrsSplit.md) |  | [optional] 
**cost_build** | [**AthleticProfileShowSportFinancialsCostBuild**](AthleticProfileShowSportFinancialsCostBuild.md) |  | [optional] 
**cost_per_win** | [**AthleticProfileShowSportFinancialsCostPerWin**](AthleticProfileShowSportFinancialsCostPerWin.md) |  | [optional] 
**dept_line** | [**AthleticProfileShowSportFinancialsDeptLine**](AthleticProfileShowSportFinancialsDeptLine.md) |  | [optional] 
**as_of** | **date** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_financials import AthleticProfileShowSportFinancials

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportFinancials from a JSON string
athletic_profile_show_sport_financials_instance = AthleticProfileShowSportFinancials.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportFinancials.to_json())

# convert the object into a dict
athletic_profile_show_sport_financials_dict = athletic_profile_show_sport_financials_instance.to_dict()
# create an instance of AthleticProfileShowSportFinancials from a dict
athletic_profile_show_sport_financials_from_dict = AthleticProfileShowSportFinancials.from_dict(athletic_profile_show_sport_financials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


