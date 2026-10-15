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
**newer_season** | [**NewerSeasonContext**](NewerSeasonContext.md) | Display-only authorized coach positions newer than this row, restricted to the application current season or current season plus one; never fall back to older seasons. Sport-scoped searches (a selected sport or conference, or a sport-specific subscription) only use this row&#39;s sport; other searches use every sport. Resolve each sport separately: use the current season when next season repeats the same school, sport and jobs (salary, title wording, type order and record IDs ignored), otherwise next season, or whichever season has jobs. Keep every job of the chosen season that is newer than this row. Return context when any of those jobs has no unchanged counterpart among this row season&#39;s jobs: a school-ID change, or at the same school both a different position-type ID set and different resolved job wording. Free-text titles override type labels; label ordering alone is ignored. Salary, free-text title, sport, and type ordering alone do not trigger context. Pure or mixed Staff Member appointments (type name INTERCOLLEGIATE_ONLY) are eligible context; other intercollegiate-only types remain excluded. Ordinary search-result exclusions are unchanged. The top-level facts describe the first ranked assignment. Does not affect selected-season fields, search membership, filters, sorting, pagination, statistics or COLI. No salary carry-forward or document links. | [optional] 
**assignments** | [**List[PersonAssignment]**](PersonAssignment.md) | Display-only authorized positions this coach holds in this row&#39;s season, ranked primary first; only this row&#39;s sport when the search is sport-scoped (see newer_season). An explicit school filter also restricts this ordinary collection to the row&#39;s school; NOW stays independent. The result row keeps its own school, sport, title and salary; this array powers only the +N disclosure and does not replace those row fields. Intercollegiate-only appointments are excluded like search membership. Empty when none are resolvable. | [optional] 
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
**latest_known_fallback** | **bool** | True when the row&#39;s position has no usable annual total but an earlier season of the same unbroken job (same coach, school, sport and position types in every season between) does, and no season since that record carries an hourly record or conflicting positions, so the latest_known_* fields carry that older record as display-only context. It never changes compensation_cents, the comp filters, the compensation sort or comp_stats, and the latest_compensation_* columns behind it are not accepted as filter or sort inputs. The whole latest_known_* group is absent without compensation access. | [optional] 
**latest_known_compensation_cents** | **int** | Total of that older record in cents; null unless latest_known_fallback. | [optional] 
**latest_known_base_salary_cents** | **int** | Base salary of that older record in cents; null unless latest_known_fallback. | [optional] 
**latest_known_compensation_type** | **str** | Compensation type as stored on that older record; null unless latest_known_fallback, and null when the record stores no type (the same raw reading as compensation_type). | [optional] 
**latest_known_source_year** | **int** | End year of the season the older record&#39;s position belongs to (2024 means 2023–24); null unless latest_known_fallback. Always earlier than the target assignment&#39;s season. | [optional] 
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


