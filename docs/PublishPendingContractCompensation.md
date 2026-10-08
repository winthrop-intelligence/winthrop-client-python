# PublishPendingContractCompensation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**year** | **int** | Four-digit year | 
**compensation_type** | **str** | A private school&#39;s compensation must be 990 | 
**base_salary** | [**PublishPendingContractCompensationBaseSalary**](PublishPendingContractCompensationBaseSalary.md) |  | [optional] 
**one_time_bonus** | [**PublishPendingContractCompensationOneTimeBonus**](PublishPendingContractCompensationOneTimeBonus.md) |  | [optional] 
**outside_income** | [**PublishPendingContractCompensationOneTimeBonus**](PublishPendingContractCompensationOneTimeBonus.md) |  | [optional] 
**deferred_compensation** | [**PublishPendingContractCompensationOneTimeBonus**](PublishPendingContractCompensationOneTimeBonus.md) |  | [optional] 
**personal_services** | [**PublishPendingContractCompensationOneTimeBonus**](PublishPendingContractCompensationOneTimeBonus.md) |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**country_club_membership** | **bool** |  | [optional] 
**car_provided** | **bool** |  | [optional] 
**comment** | **str** | Required for hourly | [optional] 
**buyout_amount** | **str** | Buyout terms, as text | [optional] 
**change_note** | **str** | Optional. Why this row&#39;s values are what they are, for the internal audit history (WINAD-10632). Stored on the audit versions of this row&#39;s compensation write; never returned by the API. Blank is the same as omitted. | [optional] 

## Example

```python
from winthrop_client_python.models.publish_pending_contract_compensation import PublishPendingContractCompensation

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPendingContractCompensation from a JSON string
publish_pending_contract_compensation_instance = PublishPendingContractCompensation.from_json(json)
# print the JSON string representation of the object
print(PublishPendingContractCompensation.to_json())

# convert the object into a dict
publish_pending_contract_compensation_dict = publish_pending_contract_compensation_instance.to_dict()
# create an instance of PublishPendingContractCompensation from a dict
publish_pending_contract_compensation_from_dict = PublishPendingContractCompensation.from_dict(publish_pending_contract_compensation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


