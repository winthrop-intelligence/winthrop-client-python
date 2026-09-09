# AthleticProfileShowSportFinancialsProgramCostPerWin

Private schools only — the program's EADA expense over the selected season's wins, against the FRS filers' program expense per win on the scatter's fiscal year. Replaces cost_per_win on the private sport Financials tab.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fiscal_year** | **int** | The EADA filing year the expense and margin come from. | [optional] 
**expense_cents** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**per_win_cents** | **int** |  | [optional] 
**margin_cents** | **int** | EADA revenue minus expense; null when the filing priced only one of them. | [optional] 
**cohort_median_per_win_cents** | **int** |  | [optional] 
**cohort_size** | **int** |  | [optional] 
**cheapest** | [**AthleticProfileShowSportFinancialsProgramCostPerWinCheapest**](AthleticProfileShowSportFinancialsProgramCostPerWinCheapest.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_financials_program_cost_per_win import AthleticProfileShowSportFinancialsProgramCostPerWin

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportFinancialsProgramCostPerWin from a JSON string
athletic_profile_show_sport_financials_program_cost_per_win_instance = AthleticProfileShowSportFinancialsProgramCostPerWin.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportFinancialsProgramCostPerWin.to_json())

# convert the object into a dict
athletic_profile_show_sport_financials_program_cost_per_win_dict = athletic_profile_show_sport_financials_program_cost_per_win_instance.to_dict()
# create an instance of AthleticProfileShowSportFinancialsProgramCostPerWin from a dict
athletic_profile_show_sport_financials_program_cost_per_win_from_dict = AthleticProfileShowSportFinancialsProgramCostPerWin.from_dict(athletic_profile_show_sport_financials_program_cost_per_win_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


