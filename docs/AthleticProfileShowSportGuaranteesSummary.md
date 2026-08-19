# AthleticProfileShowSportGuaranteesSummary

Cash for the selected season only, never the whole window — the ledger may span seasons but this totals the one the page is on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**out_cents** | **int** |  | [optional] 
**in_cents** | **int** |  | [optional] 
**agreements_count** | **int** |  | [optional] 
**priced_count** | **int** |  | [optional] 
**all_on_file** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_guarantees_summary import AthleticProfileShowSportGuaranteesSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportGuaranteesSummary from a JSON string
athletic_profile_show_sport_guarantees_summary_instance = AthleticProfileShowSportGuaranteesSummary.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportGuaranteesSummary.to_json())

# convert the object into a dict
athletic_profile_show_sport_guarantees_summary_dict = athletic_profile_show_sport_guarantees_summary_instance.to_dict()
# create an instance of AthleticProfileShowSportGuaranteesSummary from a dict
athletic_profile_show_sport_guarantees_summary_from_dict = AthleticProfileShowSportGuaranteesSummary.from_dict(athletic_profile_show_sport_guarantees_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


