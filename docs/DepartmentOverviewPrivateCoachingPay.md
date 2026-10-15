# DepartmentOverviewPrivateCoachingPay

What a private department pays its coaches (WINAD-10390), from its EADA filing's coaching tables: one row per role and team category, each `amount_cents` the combined pay of the coaches that row covers. The filing states an average salary and a headcount and never the pool, so every figure here is derived per category from those two. Rows the filing does not state are absent; null when the school has no matched EADA report, or when its filing states no usable coaching category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**rows** | [**List[DepartmentOverviewPrivateCoachingPayRow]**](DepartmentOverviewPrivateCoachingPayRow.md) |  | 

## Example

```python
from winthrop_client_python.models.department_overview_private_coaching_pay import DepartmentOverviewPrivateCoachingPay

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateCoachingPay from a JSON string
department_overview_private_coaching_pay_instance = DepartmentOverviewPrivateCoachingPay.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateCoachingPay.to_json())

# convert the object into a dict
department_overview_private_coaching_pay_dict = department_overview_private_coaching_pay_instance.to_dict()
# create an instance of DepartmentOverviewPrivateCoachingPay from a dict
department_overview_private_coaching_pay_from_dict = DepartmentOverviewPrivateCoachingPay.from_dict(department_overview_private_coaching_pay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


