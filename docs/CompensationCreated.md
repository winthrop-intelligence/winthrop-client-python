# CompensationCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**bonus_comp_cents** | **int** |  | [optional] 
**deferred_comp_cents** | **int** |  | [optional] 
**talent_fee** | **int** |  | [optional] 
**is_car_provided** | **bool** | Accepted when creating a compensation (POST) only. PATCH ignores this field. | [optional] 
**country_club_dues_cents** | **int** |  | [optional] 
**coach_id** | **int** | Required on creation. Existing coach-less records may return null. Updates may omit this field or send its unchanged value. To change an existing compensation&#39;s identity, move the linked position. | [optional] 
**contract_id** | **int** | Request field, optional. The contract to link. On creation it must be a non-pending contract of coach_id. Responses describe the linked contract in the nested contract object. | [optional] 
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
**county_club_membership_paid** | **bool** |  | [optional] 
**base_salary_cents** | **int** |  | [optional] 
**bonus_has_contingents** | **bool** |  | [optional] 
**calculated_guaranteed_comp_cents** | **int** |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**noncontingent_bonus_comp_cents** | **int** |  | [optional] 
**compensation_type** | **str** |  | [optional] 
**media_link** | **str** |  | [optional] 
**contract_status_id** | **int** |  | [optional] 
**year** | **int** | Required on creation. Updates may omit this field or send its unchanged value. To change an existing compensation&#39;s identity, move the linked position. | [optional] 
**school_id** | **int** | Required on creation. Updates may omit this field or send its unchanged value. To change an existing compensation&#39;s identity, move the linked position. | [optional] 
**contract** | [**Contract**](Contract.md) |  | [optional] 
**created_positions_count** | **int** | Number of positions copied into the year by this request. | [optional] 
**created_position_ids** | **List[int]** | Ids of the positions copied into the year by this request. | [optional] 

## Example

```python
from winthrop_client_python.models.compensation_created import CompensationCreated

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationCreated from a JSON string
compensation_created_instance = CompensationCreated.from_json(json)
# print the JSON string representation of the object
print(CompensationCreated.to_json())

# convert the object into a dict
compensation_created_dict = compensation_created_instance.to_dict()
# create an instance of CompensationCreated from a dict
compensation_created_from_dict = CompensationCreated.from_dict(compensation_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


