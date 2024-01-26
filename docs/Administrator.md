# Administrator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_first_name** | **str** |  | [optional] 
**coach_last_name** | **str** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**season_id** | **int** |  | [optional] 
**position_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**geo_division_id** | **int** |  | [optional] 
**compensation_id** | **int** |  | [optional] 
**contract_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**position_title** | **str** |  | [optional] 
**school_name** | **str** |  | [optional] 
**school_short_name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**usnwr_ranking** | **int** |  | [optional] 
**directors_cup_ranking** | **int** |  | [optional] 
**compensation_cents** | **int** |  | [optional] 
**compensation_base_salary_cents** | **int** |  | [optional] 
**compensation_type** | **str** |  | [optional] 
**compensation_outside_income_cents** | **int** |  | [optional] 
**compensation_deferred_comp_cents** | **int** |  | [optional] 
**compensation_one_time_bonus_cents** | **int** |  | [optional] 
**compensation_contingent_bonus_comp_cents** | **int** |  | [optional] 
**compensation_buyout_terms** | **str** |  | [optional] 
**compensation_num_cars** | **int** |  | [optional] 
**compensation_car_stipend_cents** | **int** |  | [optional] 
**compensation_country_club_dues_cents** | **int** |  | [optional] 
**compensation_country_club_membership_paid** | **bool** |  | [optional] 
**compensation_media_link** | **str** |  | [optional] 
**contract_starts_on** | **date** |  | [optional] 
**contract_expires_on** | **date** |  | [optional] 
**diversity** | **bool** |  | [optional] 
**gender** | **str** |  | [optional] 
**alma_mater_id** | **int** |  | [optional] 
**private** | **bool** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**coli** | **float** |  | [optional] 
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
print Administrator.to_json()

# convert the object into a dict
administrator_dict = administrator_instance.to_dict()
# create an instance of Administrator from a dict
administrator_form_dict = administrator.from_dict(administrator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


