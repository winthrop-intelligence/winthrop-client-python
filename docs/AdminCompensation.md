# AdminCompensation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**compensation_type** | **str** |  | [optional] 
**base_salary_dollars** | **str** |  | [optional] 
**one_time_bonus_dollars** | **str** |  | [optional] 
**talent_fee_dollars** | **str** |  | [optional] 
**outside_income_dollars** | **str** |  | [optional] 
**deferred_comp_dollars** | **str** |  | [optional] 
**buyout_terms** | **str** |  | [optional] 
**is_car_provided** | **bool** |  | [optional] 
**county_club_membership_paid** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 
**contract_status_id** | **int** |  | [optional] 
**contract_id** | **int** |  | [optional] 
**media_link** | **str** |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**persisted** | **bool** |  | [optional] 
**calculated_guaranteed_comp_dollars** | **str** |  | [optional] 
**salary_str** | **str** |  | [optional] 
**has_raw_contract** | **bool** |  | [optional] 
**formatted_buyout_terms** | **str** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**school** | [**AdminCoachCurrentSchool**](AdminCoachCurrentSchool.md) |  | [optional] 
**contract_status** | [**AdminCoachHometownState**](AdminCoachHometownState.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_compensation import AdminCompensation

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCompensation from a JSON string
admin_compensation_instance = AdminCompensation.from_json(json)
# print the JSON string representation of the object
print(AdminCompensation.to_json())

# convert the object into a dict
admin_compensation_dict = admin_compensation_instance.to_dict()
# create an instance of AdminCompensation from a dict
admin_compensation_from_dict = AdminCompensation.from_dict(admin_compensation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


