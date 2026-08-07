# DepartmentOverviewPrivateAdComp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** |  | 
**fiscal_year** | **int** |  | 
**basis** | **str** |  | 

## Example

```python
from winthrop_client_python.models.department_overview_private_ad_comp import DepartmentOverviewPrivateAdComp

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateAdComp from a JSON string
department_overview_private_ad_comp_instance = DepartmentOverviewPrivateAdComp.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateAdComp.to_json())

# convert the object into a dict
department_overview_private_ad_comp_dict = department_overview_private_ad_comp_instance.to_dict()
# create an instance of DepartmentOverviewPrivateAdComp from a dict
department_overview_private_ad_comp_from_dict = DepartmentOverviewPrivateAdComp.from_dict(department_overview_private_ad_comp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


