# DepartmentOverviewPrivateCoachingPayRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**label** | **str** |  | 
**coach_count** | **int** |  | 
**amount_cents** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_overview_private_coaching_pay_row import DepartmentOverviewPrivateCoachingPayRow

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateCoachingPayRow from a JSON string
department_overview_private_coaching_pay_row_instance = DepartmentOverviewPrivateCoachingPayRow.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateCoachingPayRow.to_json())

# convert the object into a dict
department_overview_private_coaching_pay_row_dict = department_overview_private_coaching_pay_row_instance.to_dict()
# create an instance of DepartmentOverviewPrivateCoachingPayRow from a dict
department_overview_private_coaching_pay_row_from_dict = DepartmentOverviewPrivateCoachingPayRow.from_dict(department_overview_private_coaching_pay_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


