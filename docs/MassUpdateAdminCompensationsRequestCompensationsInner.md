# MassUpdateAdminCompensationsRequestCompensationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**base_salary_dollars** | **str** |  | [optional] 
**one_time_bonus_dollars** | **str** |  | [optional] 
**relocation_dollars** | **str** | The relocation amount in dollars. Blank or null clears it (and the flag with it). | [optional] 
**relocation_taxable** | **bool** | Whether the relocation is taxable income. Required when relocation_dollars is set; ignored (stored as null) when it is blank. | [optional] 
**talent_fee_dollars** | **str** |  | [optional] 
**outside_income_dollars** | **str** |  | [optional] 
**deferred_comp_dollars** | **str** |  | [optional] 
**buyout_terms** | **str** |  | [optional] 
**is_car_provided** | **bool** |  | [optional] 
**county_club_membership_paid** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 
**contract_status_id** | **int** | Omit or send null for a new row to retain its default status. | [optional] 
**contract_id** | **int** |  | [optional] 
**compensation_type** | **str** |  | [optional] 
**media_link** | **str** |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.mass_update_admin_compensations_request_compensations_inner import MassUpdateAdminCompensationsRequestCompensationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MassUpdateAdminCompensationsRequestCompensationsInner from a JSON string
mass_update_admin_compensations_request_compensations_inner_instance = MassUpdateAdminCompensationsRequestCompensationsInner.from_json(json)
# print the JSON string representation of the object
print(MassUpdateAdminCompensationsRequestCompensationsInner.to_json())

# convert the object into a dict
mass_update_admin_compensations_request_compensations_inner_dict = mass_update_admin_compensations_request_compensations_inner_instance.to_dict()
# create an instance of MassUpdateAdminCompensationsRequestCompensationsInner from a dict
mass_update_admin_compensations_request_compensations_inner_from_dict = MassUpdateAdminCompensationsRequestCompensationsInner.from_dict(mass_update_admin_compensations_request_compensations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


