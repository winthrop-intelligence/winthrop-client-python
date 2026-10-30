# Administrator

Administrator search result. In /administrator_searches responses, compensation fields are only included when the user has administrator_compensation permission, and contract fields are only included when the user can view the related contract or raw contract.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_known_fallback** | **bool** | True when the row&#39;s position has no usable annual total but an earlier season of the same unbroken job (same coach, school, sport and position types in every season between) does, and no season since that record carries an hourly record or conflicting positions, so the latest_known_* fields carry that older record as display-only context. It never changes compensation_cents, the comp filters, the compensation sort or comp_stats, and the latest_compensation_* columns behind it are not accepted as filter or sort inputs. The whole latest_known_* group is absent without compensation access. | [optional] 
**latest_known_compensation_cents** | **int** | Total of that older record in cents; null unless latest_known_fallback. | [optional] 
**latest_known_base_salary_cents** | **int** | Base salary of that older record in cents; null unless latest_known_fallback. | [optional] 
**latest_known_compensation_type** | **str** | Compensation type as stored on that older record; null unless latest_known_fallback, and null when the record stores no type (the same raw reading as compensation_type). | [optional] 
**latest_known_source_year** | **int** | End year of the season the older record&#39;s position belongs to (2024 means 2023–24); null unless latest_known_fallback. Always earlier than the target assignment&#39;s season. | [optional] 
**latest_known_source_compensation_id** | **int** | The older compensation record&#39;s id; null unless latest_known_fallback. | [optional] 
**latest_known_source_raw_contract_id** | **int** | The document behind the older record, present only when one is on file and the viewer may open it. Distinct from raw_contract_id, which stays the current position&#39;s contract document. | [optional] 
**id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_first_name** | **str** |  | [optional] 
**coach_last_name** | **str** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**name** | **str** | Combined display name (first + last) | [optional] 
**season_id** | **int** |  | [optional] 
**position_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**geo_division_id** | **int** |  | [optional] 
**compensation_id** | **int** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**contract_id** | **int** | Only included in /administrator_searches responses when the user can view this administrator&#39;s contract. | [optional] 
**year** | **int** |  | [optional] 
**newer_season** | [**NewerSeasonContext**](NewerSeasonContext.md) | Display-only authorized administrator assignments newer than this row, restricted to the application current season or current season plus one; never fall back to older seasons. Resolve each sport separately: use the current season when next season repeats the same school, sport and jobs (salary, title wording, type order and record IDs ignored), otherwise next season, or whichever season has jobs. Keep every job of the chosen season that is newer than this row. Return context when any of those jobs has no unchanged counterpart among this row season&#39;s jobs: a school-ID change, or at the same school both a different position-type ID set and different resolved job wording. Free-text titles override type labels; label ordering alone is ignored. Salary, title wording, sport and type order alone do not trigger context. Pure or mixed Staff Member appointments (type name INTERCOLLEGIATE_ONLY) are eligible context; other intercollegiate-only types remain excluded. Ordinary search-result exclusions are unchanged. The top-level facts describe the first ranked assignment. Administrator salary permissions apply; no salary carry-forward or document links. Does not change selected-season fields, search membership, filters, sorting, pagination or statistics. | [optional] 
**assignments** | [**List[PersonAssignment]**](PersonAssignment.md) | Display-only authorized ADMIN assignments this administrator holds in this row&#39;s season (its school, ADMIN sport and year), ranked primary first. Non-ADMIN appointments belong to Coach Search rather than this collection. The result row keeps its own school, sport, title and salary; this array powers only the +N disclosure and does not replace those row fields. Intercollegiate-only appointments are excluded like search membership. Empty when none are resolvable. | [optional] 
**position_title** | **str** |  | [optional] 
**school_name** | **str** |  | [optional] 
**school_short_name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**usnwr_ranking** | **int** |  | [optional] 
**directors_cup_ranking** | **int** |  | [optional] 
**compensation_cents** | **int** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_base_salary_cents** | **int** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_type** | **str** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_outside_income_cents** | **int** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_deferred_comp_cents** | **int** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_one_time_bonus_cents** | **int** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_relocation_cents** | **int** | The relocation amount, separate from the one-time bonus (WINAD-10700). Null when there is none. Counted in compensation_cents only when compensation_relocation_taxable is true. Included under the same administrator_compensation permission as the other compensation fields. | [optional] 
**compensation_relocation_taxable** | **bool** | Whether the relocation is taxable income. Null exactly when compensation_relocation_cents is null. | [optional] 
**compensation_contingent_bonus** | **bool** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_buyout_terms** | **str** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_is_car_provided** | **bool** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_country_club_dues_cents** | **int** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_country_club_membership_paid** | **bool** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_talent_fee** | **int** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**compensation_media_link** | **str** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**raw_contract_id** | **int** | Only included in /administrator_searches responses when the user can view this administrator&#39;s raw contract. | [optional] 
**contract_starts_on** | **date** | Only included in /administrator_searches responses when the user can view this administrator&#39;s contract. | [optional] 
**contract_expires_on** | **date** | Only included in /administrator_searches responses when the user can view this administrator&#39;s contract. | [optional] 
**contract_at_will** | **bool** | Only included in /administrator_searches responses when the user can view this administrator&#39;s contract. | [optional] 
**diversity** | **bool** |  | [optional] 
**gender** | **str** |  | [optional] 
**alma_mater_id** | **int** |  | [optional] 
**private** | **bool** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**coli** | **float** | Only included in /administrator_searches responses when the user has administrator_compensation permission. | [optional] 
**coach** | [**Coach**](Coach.md) |  | [optional] 
**departments** | [**List[PositionType]**](PositionType.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.administrator import Administrator

# TODO update the JSON string below
json = "{}"
# create an instance of Administrator from a JSON string
administrator_instance = Administrator.from_json(json)
# print the JSON string representation of the object
print(Administrator.to_json())

# convert the object into a dict
administrator_dict = administrator_instance.to_dict()
# create an instance of Administrator from a dict
administrator_from_dict = Administrator.from_dict(administrator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


