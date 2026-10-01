# CompensationCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**school_id** | **int** |  | 
**year** | **int** | Four-digit year, at most 15 years ahead | 
**contract_id** | **int** | A non-pending contract of the same coach | [optional] 
**contract_status_id** | **int** | Defaults to COMPLETE when a contract is linked | [optional] 
**compensation_type** | **str** |  | [optional] 
**base_salary_cents** | **int** |  | [optional] 
**one_time_bonus_cents** | **int** |  | [optional] 
**outside_income_cents** | **int** |  | [optional] 
**deferred_comp_cents** | **int** |  | [optional] 
**guaranteed_comp_cents** | **int** |  | [optional] 
**bonus_comp_cents** | **int** |  | [optional] 
**noncontingent_bonus_comp_cents** | **int** |  | [optional] 
**calculated_guaranteed_comp_cents** | **int** |  | [optional] 
**average_yearly_comp_cents** | **int** |  | [optional] 
**car_stipend_cents** | **int** |  | [optional] 
**country_club_dues_cents** | **int** |  | [optional] 
**talent_fee** | **int** |  | [optional] 
**num_cars** | **int** |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**bonus_has_contingents** | **bool** |  | [optional] 
**county_club_membership_paid** | **bool** |  | [optional] 
**is_car_provided** | **bool** | Accepted on creation only | [optional] 
**executed_on** | **date** |  | [optional] 
**start_on** | **date** |  | [optional] 
**end_on** | **date** |  | [optional] 
**expires_on** | **date** |  | [optional] 
**buyout_terms** | **str** |  | [optional] 
**media_link** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.compensation_create_request import CompensationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationCreateRequest from a JSON string
compensation_create_request_instance = CompensationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CompensationCreateRequest.to_json())

# convert the object into a dict
compensation_create_request_dict = compensation_create_request_instance.to_dict()
# create an instance of CompensationCreateRequest from a dict
compensation_create_request_from_dict = CompensationCreateRequest.from_dict(compensation_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


