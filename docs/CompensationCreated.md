# CompensationCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_note** | **str** | Write-only (PATCH; POST takes it beside &#x60;compensation&#x60;). Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 
**id** | **int** |  | [optional] 
**bonus_comp_cents** | **int** |  | [optional] 
**deferred_comp_cents** | **int** |  | [optional] 
**talent_fee** | **int** |  | [optional] 
**is_car_provided** | **bool** | Accepted on POST and PATCH. Must be a JSON boolean (true/false) or, as in POST, the strings \&quot;true\&quot;/\&quot;false\&quot;/\&quot;1\&quot;/\&quot;0\&quot; and the integers 1/0. PATCH is stricter than POST - it refuses null, \&quot;\&quot; and floats (0.0, 1.0), which POST accepts and converts - and answers 422 (errors.is_car_provided). | [optional] 
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
**relocation_cents** | **int** | The relocation amount in cents, separate from one_time_bonus_cents. Counted in calculated_guaranteed_comp_cents only when relocation_taxable is true; a non-taxable amount is stored and shown but stays out of the total. Requires relocation_taxable whenever it is set (422 on relocation_taxable otherwise). A whole number of cents on writes, non-negative and at most 9223372036854775807 (a bigint, unlike the 32-bit amounts beside it); a taxable amount must also keep calculated_guaranteed_comp_cents within 2147483647 (422 on calculated_guaranteed_comp_cents otherwise). Null or omitted when there is no relocation. | [optional] 
**relocation_taxable** | **bool** | Whether the relocation is taxable income. Required (true or false) when relocation_cents is set and null when it is not; there is no default, so an unknown value is never counted as income. On writes it must be a JSON boolean (or \&quot;true\&quot;/\&quot;false\&quot;/\&quot;1\&quot;/\&quot;0\&quot;), anything else is a 422. | [optional] 
**comment** | **str** |  | [optional] 
**county_club_membership_paid** | **bool** |  | [optional] 
**base_salary_cents** | **int** |  | [optional] 
**bonus_has_contingents** | **bool** |  | [optional] 
**calculated_guaranteed_comp_cents** | **int** |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**noncontingent_bonus_comp_cents** | **int** |  | [optional] 
**compensation_type** | **str** | Pay type, writable on PATCH. Hourly rows require blank/zero amounts and a non-blank comment holding the hourly rate (or &#39;Hourly rate not provided&#39;). Private-school compensations must be \&quot;990\&quot;. | [optional] 
**media_link** | **str** |  | [optional] 
**contract_status_id** | **int** | Writable on PATCH, any existing contract status id; see PATCH description. | [optional] 
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


