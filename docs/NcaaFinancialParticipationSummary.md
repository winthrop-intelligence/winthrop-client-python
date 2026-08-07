# NcaaFinancialParticipationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_contract_id** | **int** |  | 
**gender** | **str** |  | 
**total_participants** | **int** |  | 
**second_team_participants** | **int** |  | 
**third_team_participants** | **int** |  | 
**unduplicated_participants** | **int** |  | 
**participant_proportion** | **str** | Exact decimal representation of the source participant proportion. | 

## Example

```python
from winthrop_client_python.models.ncaa_financial_participation_summary import NcaaFinancialParticipationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NcaaFinancialParticipationSummary from a JSON string
ncaa_financial_participation_summary_instance = NcaaFinancialParticipationSummary.from_json(json)
# print the JSON string representation of the object
print(NcaaFinancialParticipationSummary.to_json())

# convert the object into a dict
ncaa_financial_participation_summary_dict = ncaa_financial_participation_summary_instance.to_dict()
# create an instance of NcaaFinancialParticipationSummary from a dict
ncaa_financial_participation_summary_from_dict = NcaaFinancialParticipationSummary.from_dict(ncaa_financial_participation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


