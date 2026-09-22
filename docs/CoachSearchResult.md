# CoachSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Coach ID | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**school_name** | **str** |  | [optional] 
**school_short_name** | **str** |  | [optional] 
**school_id** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**division_name** | **str** |  | [optional] 
**division_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**coach_friendly_id** | **str** |  | [optional] 
**visible** | **bool** | Whether the coach appears on customer-facing surfaces | [optional] 
**position_types** | **List[str]** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**sport_full_name** | **str** |  | [optional] 
**position_title** | **str** |  | [optional] 
**season_wins** | **int** |  | [optional] 
**season_losses** | **int** |  | [optional] 
**season_ties** | **int** |  | [optional] 
**season_conference_position** | **int** |  | [optional] 
**season_conference_num_positions** | **int** |  | [optional] 
**rpi** | **float** |  | [optional] 
**net_rank** | **float** |  | [optional] 
**ap_rank** | **float** |  | [optional] 
**compensation_cents** | **int** | Total compensation in cents (included based on authorization) | [optional] 
**base_salary_cents** | **int** | Base salary in cents (included based on authorization) | [optional] 
**coli** | **float** | School&#39;s cost-of-living index (included based on authorization) | [optional] 
**compensation_type** | **str** | Compensation type (included based on authorization) | [optional] 
**compensation_contingent_bonus** | **bool** |  | [optional] 
**compensation_deferred_comp_cents** | **int** |  | [optional] 
**compensation_one_time_bonus_cents** | **int** |  | [optional] 
**compensation_buyout_terms** | **str** |  | [optional] 
**compensation_is_car_provided** | **bool** |  | [optional] 
**compensation_outside_income_cents** | **int** |  | [optional] 
**compensation_talent_fee** | **int** |  | [optional] 
**compensation_county_club_membership_paid** | **bool** |  | [optional] 
**compensation_media_link** | **str** |  | [optional] 
**latest_known_fallback** | **bool** | True when the searched season has no usable annual total for this assignment but an earlier season of the same unbroken job (same coach, school, sport and position types in every season between) does, so the latest_known_* fields carry that older record as display-only context (included based on authorization). It never changes compensation_cents, the comp filters, the compensation sort or comp_stats. | [optional] 
**latest_known_compensation_cents** | **int** | Total of that older record in cents; null unless latest_known_fallback. | [optional] 
**latest_known_base_salary_cents** | **int** | Base salary of that older record in cents; null unless latest_known_fallback. | [optional] 
**latest_known_compensation_type** | **str** | Compensation type of that older record; null unless latest_known_fallback. | [optional] 
**latest_known_source_year** | **int** | Season end year the older record was filed for (2024 means 2023–24); null unless latest_known_fallback. Always earlier than year. | [optional] 
**latest_known_source_compensation_id** | **int** | The older compensation record&#39;s id; null unless latest_known_fallback. | [optional] 
**latest_known_source_raw_contract_id** | **int** | The document behind the older record, present only when one is on file and the viewer may open it. Distinct from raw_contract_id, which stays the current position&#39;s contract document. | [optional] 
**contract_starts_on** | **date** |  | [optional] 
**contract_expires_on** | **date** |  | [optional] 
**contract_at_will** | **bool** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_search_result import CoachSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of CoachSearchResult from a JSON string
coach_search_result_instance = CoachSearchResult.from_json(json)
# print the JSON string representation of the object
print(CoachSearchResult.to_json())

# convert the object into a dict
coach_search_result_dict = coach_search_result_instance.to_dict()
# create an instance of CoachSearchResult from a dict
coach_search_result_from_dict = CoachSearchResult.from_dict(coach_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


