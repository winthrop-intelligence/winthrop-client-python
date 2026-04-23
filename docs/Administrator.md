# Administrator

Administrator search result. In /administrator_searches responses, compensation fields are only included when the user has administrator_compensation permission, and contract fields are only included when the user can view the related contract or raw contract.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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


