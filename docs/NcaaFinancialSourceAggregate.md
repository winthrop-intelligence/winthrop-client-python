# NcaaFinancialSourceAggregate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_contract_id** | **int** |  | 
**source_label** | **str** |  | 
**gender** | **str** |  | 
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
from winthrop_client_python.models.ncaa_financial_source_aggregate import NcaaFinancialSourceAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of NcaaFinancialSourceAggregate from a JSON string
ncaa_financial_source_aggregate_instance = NcaaFinancialSourceAggregate.from_json(json)
# print the JSON string representation of the object
print(NcaaFinancialSourceAggregate.to_json())

# convert the object into a dict
ncaa_financial_source_aggregate_dict = ncaa_financial_source_aggregate_instance.to_dict()
# create an instance of NcaaFinancialSourceAggregate from a dict
ncaa_financial_source_aggregate_from_dict = NcaaFinancialSourceAggregate.from_dict(ncaa_financial_source_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


