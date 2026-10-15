# AthleticProfileShowSportFinancialsEadaSportLine

This program's money as the school's federal EADA filing reports it (WINAD-10403). Present only for private schools, which file no NCAA FRS sport split and never will — for them this is the sport's money, not a substitute for a filing that is still coming. Null for public schools, and for a private school with no matched EADA sport row or no EADA grant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fiscal_year** | **int** | The EADA reporting year these figures were filed for. | [optional] 
**expense_cents** | **int** |  | [optional] 
**revenue_cents** | **int** |  | [optional] 
**operating_expense_cents** | **int** | Game-day operating expense for this program&#39;s own gender (EADA OPEXPPERTEAM_MEN/_WOMEN), not the row&#39;s combined men&#39;s-and-women&#39;s total. | [optional] 
**participants** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_financials_eada_sport_line import AthleticProfileShowSportFinancialsEadaSportLine

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportFinancialsEadaSportLine from a JSON string
athletic_profile_show_sport_financials_eada_sport_line_instance = AthleticProfileShowSportFinancialsEadaSportLine.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportFinancialsEadaSportLine.to_json())

# convert the object into a dict
athletic_profile_show_sport_financials_eada_sport_line_dict = athletic_profile_show_sport_financials_eada_sport_line_instance.to_dict()
# create an instance of AthleticProfileShowSportFinancialsEadaSportLine from a dict
athletic_profile_show_sport_financials_eada_sport_line_from_dict = AthleticProfileShowSportFinancialsEadaSportLine.from_dict(athletic_profile_show_sport_financials_eada_sport_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


