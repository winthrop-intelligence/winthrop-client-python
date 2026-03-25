# CoachCompensationTabCompensationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year_str** | **str** |  | 
**school_name** | **str** |  | 
**school_id** | **int** |  | 
**position_sport** | **str** |  | 
**total_cents** | **int** |  | [optional] 
**base_salary_cents** | **int** |  | [optional] 
**talent_fee_cents** | **int** |  | [optional] 
**deferred_comp_cents** | **int** |  | [optional] 
**compensation_type** | **str** |  | 
**media_link** | **str** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_compensation_tab_compensations_inner import CoachCompensationTabCompensationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensationTabCompensationsInner from a JSON string
coach_compensation_tab_compensations_inner_instance = CoachCompensationTabCompensationsInner.from_json(json)
# print the JSON string representation of the object
print(CoachCompensationTabCompensationsInner.to_json())

# convert the object into a dict
coach_compensation_tab_compensations_inner_dict = coach_compensation_tab_compensations_inner_instance.to_dict()
# create an instance of CoachCompensationTabCompensationsInner from a dict
coach_compensation_tab_compensations_inner_from_dict = CoachCompensationTabCompensationsInner.from_dict(coach_compensation_tab_compensations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


