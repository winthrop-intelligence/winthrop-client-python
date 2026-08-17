# AthleticProfileShowSportGuarantees

Guarantees tab payload for a sport scope (WINAD-10209); null for ADMIN scope or without game-contract access. Every amount comes from a filed agreement — duplicate filings are included, never merged. Missing values are null, never zero.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**basketball** | **bool** |  | [optional] 
**results_lens** | **str** | The results metric this surface is read through, resolved per season from the sport&#39;s rank chain (NET for basketball, CONF_WINS for football, RPI otherwise) with CONF_WINS as the fallback when no rank is filed (WINAD-10259, WINAD-10268). Metric fields ship for every column; the lens names the one a surface may claim. | [optional] 
**agreements** | [**List[AthleticProfileShowSportGuaranteesAgreementsInner]**](AthleticProfileShowSportGuaranteesAgreementsInner.md) | The ledger, in reading order — every filed agreement inside agreement_window, the current season first, the forward book downward from it, and the seasons already played last (WINAD-10281). | [optional] 
**agreement_window** | [**AthleticProfileShowSportGuaranteesAgreementWindow**](AthleticProfileShowSportGuaranteesAgreementWindow.md) |  | [optional] 
**summary** | [**AthleticProfileShowSportGuaranteesSummary**](AthleticProfileShowSportGuaranteesSummary.md) |  | [optional] 
**quadrant** | [**AthleticProfileShowSportGuaranteesQuadrant**](AthleticProfileShowSportGuaranteesQuadrant.md) |  | [optional] 
**as_of** | **date** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_guarantees import AthleticProfileShowSportGuarantees

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportGuarantees from a JSON string
athletic_profile_show_sport_guarantees_instance = AthleticProfileShowSportGuarantees.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportGuarantees.to_json())

# convert the object into a dict
athletic_profile_show_sport_guarantees_dict = athletic_profile_show_sport_guarantees_instance.to_dict()
# create an instance of AthleticProfileShowSportGuarantees from a dict
athletic_profile_show_sport_guarantees_from_dict = AthleticProfileShowSportGuarantees.from_dict(athletic_profile_show_sport_guarantees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


