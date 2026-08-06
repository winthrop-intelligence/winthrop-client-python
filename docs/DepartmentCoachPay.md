# DepartmentCoachPay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** |  | 
**basis** | **str** |  | 
**basis_fiscal_year** | **int** |  | 
**pending_verification** | **bool** |  | 
**has_filed_contract** | **bool** |  | 
**rank** | **int** |  | 
**cohort_size** | **int** |  | 
**partial_cohort** | **bool** |  | 
**rank_withheld_reason** | **str** |  | 

## Example

```python
from winthrop_client_python.models.department_coach_pay import DepartmentCoachPay

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachPay from a JSON string
department_coach_pay_instance = DepartmentCoachPay.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachPay.to_json())

# convert the object into a dict
department_coach_pay_dict = department_coach_pay_instance.to_dict()
# create an instance of DepartmentCoachPay from a dict
department_coach_pay_from_dict = DepartmentCoachPay.from_dict(department_coach_pay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


