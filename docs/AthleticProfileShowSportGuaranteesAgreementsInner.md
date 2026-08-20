# AthleticProfileShowSportGuaranteesAgreementsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**season_year** | **int** | The season this agreement belongs to. Equal to season_year at the top level for every sport but football, whose ledger spans agreement_window. | [optional] 
**opponent_id** | **int** |  | [optional] 
**opponent_name** | **str** |  | [optional] 
**opponent_short_name** | **str** |  | [optional] 
**is_home** | **bool** |  | [optional] 
**game_type** | **str** |  | [optional] 
**game_date** | **date** |  | [optional] 
**game_date_tbd** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**comp_tbd** | **bool** |  | [optional] 
**off_site_location** | **str** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_guarantees_agreements_inner import AthleticProfileShowSportGuaranteesAgreementsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportGuaranteesAgreementsInner from a JSON string
athletic_profile_show_sport_guarantees_agreements_inner_instance = AthleticProfileShowSportGuaranteesAgreementsInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportGuaranteesAgreementsInner.to_json())

# convert the object into a dict
athletic_profile_show_sport_guarantees_agreements_inner_dict = athletic_profile_show_sport_guarantees_agreements_inner_instance.to_dict()
# create an instance of AthleticProfileShowSportGuaranteesAgreementsInner from a dict
athletic_profile_show_sport_guarantees_agreements_inner_from_dict = AthleticProfileShowSportGuaranteesAgreementsInner.from_dict(athletic_profile_show_sport_guarantees_agreements_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


