# NcaaFinancialStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | 
**sport_name** | **str** |  | 
**gender_code** | **str** |  | 
**source_sport_name** | **str** |  | 
**raw_contract_id** | **int** |  | 
**athletic_aid_equivalency** | **str** | Exact decimal representation of item 20 Part A. | 
**exhausted_eligibility_or_medical_equivalency** | **str** | Exact decimal representation of item 20 Part B. | 
**equivalencies_awarded** | **str** | Exact decimal representation of item 20 Parts A and B combined. | 
**students_receiving_athletic_aid** | **int** |  | 
**head_coach_positions** | **int** |  | 
**head_coach_fte** | **str** | Exact decimal representation of item 22 head-coach FTE. | 
**assistant_coach_positions** | **int** |  | 
**assistant_coach_fte** | **str** | Exact decimal representation of item 22 assistant-coach FTE. | 
**first_team_participants** | **int** |  | 
**second_team_participants** | **int** |  | 
**third_team_participants** | **int** |  | 

## Example

```python
from winthrop_client_python.models.ncaa_financial_stat import NcaaFinancialStat

# TODO update the JSON string below
json = "{}"
# create an instance of NcaaFinancialStat from a JSON string
ncaa_financial_stat_instance = NcaaFinancialStat.from_json(json)
# print the JSON string representation of the object
print(NcaaFinancialStat.to_json())

# convert the object into a dict
ncaa_financial_stat_dict = ncaa_financial_stat_instance.to_dict()
# create an instance of NcaaFinancialStat from a dict
ncaa_financial_stat_from_dict = NcaaFinancialStat.from_dict(ncaa_financial_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


