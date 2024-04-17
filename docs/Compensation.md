# Compensation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**bonus_comp_cents** | **int** |  | [optional] 
**deferred_comp_cents** | **int** |  | [optional] 
**talent_fee** | **int** |  | [optional] 
**num_cars** | **int** |  | [optional] 
**country_club_dues_cents** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**buyout_terms** | **str** |  | [optional] 
**executed_on** | **datetime** |  | [optional] 
**expires_on** | **datetime** |  | [optional] 
**start_on** | **datetime** |  | [optional] 
**end_on** | **datetime** |  | [optional] 
**average_yearly_comp_cents** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**outside_income_cents** | **int** |  | [optional] 
**one_time_bonus_cents** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**car_stipend_cents** | **int** |  | [optional] 
**country_club_membership_paid** | **bool** |  | [optional] 
**base_salary_cents** | **int** |  | [optional] 
**bonus_has_contingents** | **bool** |  | [optional] 
**calculated_guaranteed_comp_cents** | **int** |  | [optional] 
**contingent_bonus_comp_cents** | **int** |  | [optional] 
**noncontingent_bonus_comp_cents** | **int** |  | [optional] 
**compensation_type** | **str** |  | [optional] 
**media_link** | **str** |  | [optional] 
**contract_status_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**contract** | [**Contract**](Contract.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.compensation import Compensation

# TODO update the JSON string below
json = "{}"
# create an instance of Compensation from a JSON string
compensation_instance = Compensation.from_json(json)
# print the JSON string representation of the object
print(Compensation.to_json())

# convert the object into a dict
compensation_dict = compensation_instance.to_dict()
# create an instance of Compensation from a dict
compensation_form_dict = compensation.from_dict(compensation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


