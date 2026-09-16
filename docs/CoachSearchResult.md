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
**compensation_cents** | **int** | Total compensation in cents (included based on authorization). On a search of the current season this is the latest known salary for the row&#39;s assignment (WINAD-10478): the season&#39;s own record when it carries a usable total, otherwise the most recent usable record from the same coach, school, sport and position types up to two seasons back. Any other season reports that season&#39;s own record. The comp filters, the compensation sort and comp_stats read the same value. | [optional] 
**base_salary_cents** | **int** | Base salary in cents (included based on authorization), read from the same record as compensation_cents. | [optional] 
**coli** | **float** | School&#39;s cost-of-living index (included based on authorization) | [optional] 
**compensation_type** | **str** | Compensation type (included based on authorization), read from the same record as compensation_cents; so are the compensation_* component fields below. | [optional] 
**compensation_contingent_bonus** | **bool** |  | [optional] 
**compensation_deferred_comp_cents** | **int** |  | [optional] 
**compensation_one_time_bonus_cents** | **int** |  | [optional] 
**compensation_buyout_terms** | **str** |  | [optional] 
**compensation_is_car_provided** | **bool** |  | [optional] 
**compensation_outside_income_cents** | **int** |  | [optional] 
**compensation_talent_fee** | **int** |  | [optional] 
**compensation_county_club_membership_paid** | **bool** |  | [optional] 
**compensation_media_link** | **str** |  | [optional] 
**compensation_source_year** | **int** | Season end year of the compensation record the figures come from (included based on authorization; null when no record is on file). Equals year unless compensation_is_fallback is true. | [optional] 
**compensation_is_fallback** | **bool** | True when the figures were carried forward from an earlier season of the same assignment because the current season has no usable record (included based on authorization). Always false outside the current season. | [optional] 
**compensation_source_compensation_id** | **int** | The compensation record the figures come from (included based on authorization). | [optional] 
**compensation_source_raw_contract_id** | **int** | The document behind that record, when one is on file and the viewer may open it. Distinct from raw_contract_id, which stays the current position&#39;s contract document. | [optional] 
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


