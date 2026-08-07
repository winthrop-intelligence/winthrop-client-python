# DepartmentOverviewPrivateSpend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** |  | 
**year** | **int** |  | 
**basis** | **str** |  | 
**rank_withheld** | **bool** | EADA totals are not FRS totals, so no conference rank is computed. | 

## Example

```python
from winthrop_client_python.models.department_overview_private_spend import DepartmentOverviewPrivateSpend

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateSpend from a JSON string
department_overview_private_spend_instance = DepartmentOverviewPrivateSpend.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateSpend.to_json())

# convert the object into a dict
department_overview_private_spend_dict = department_overview_private_spend_instance.to_dict()
# create an instance of DepartmentOverviewPrivateSpend from a dict
department_overview_private_spend_from_dict = DepartmentOverviewPrivateSpend.from_dict(department_overview_private_spend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


