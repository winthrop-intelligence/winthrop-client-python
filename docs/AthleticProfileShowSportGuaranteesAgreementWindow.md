# AthleticProfileShowSportGuaranteesAgreementWindow

The span of seasons the agreements array covers (WINAD-10281). Football books guarantee games years ahead, so its ledger runs two seasons back from the current season through the last season with a filed agreement, and does not follow the season toggle. Every other sport covers the selected season alone. Derived, never fixed — a newly filed agreement a season further out extends to_year with no code change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_year** | **int** |  | [optional] 
**to_year** | **int** | The furthest season actually on file within the window; equal to from_year when the ledger is empty. | [optional] 
**multi_season** | **bool** | True when the ledger spans seasons and therefore does not repaint on a season step — the surface must say so. | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_guarantees_agreement_window import AthleticProfileShowSportGuaranteesAgreementWindow

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportGuaranteesAgreementWindow from a JSON string
athletic_profile_show_sport_guarantees_agreement_window_instance = AthleticProfileShowSportGuaranteesAgreementWindow.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportGuaranteesAgreementWindow.to_json())

# convert the object into a dict
athletic_profile_show_sport_guarantees_agreement_window_dict = athletic_profile_show_sport_guarantees_agreement_window_instance.to_dict()
# create an instance of AthleticProfileShowSportGuaranteesAgreementWindow from a dict
athletic_profile_show_sport_guarantees_agreement_window_from_dict = AthleticProfileShowSportGuaranteesAgreementWindow.from_dict(athletic_profile_show_sport_guarantees_agreement_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


