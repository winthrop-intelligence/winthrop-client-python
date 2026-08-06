# DepartmentFinancialsEadaRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**men** | [**DepartmentFinancialsEadaCategory**](DepartmentFinancialsEadaCategory.md) |  | 
**women** | [**DepartmentFinancialsEadaCategory**](DepartmentFinancialsEadaCategory.md) |  | 
**coed** | [**DepartmentFinancialsEadaCategory**](DepartmentFinancialsEadaCategory.md) |  | 

## Example

```python
from winthrop_client_python.models.department_financials_eada_role import DepartmentFinancialsEadaRole

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsEadaRole from a JSON string
department_financials_eada_role_instance = DepartmentFinancialsEadaRole.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsEadaRole.to_json())

# convert the object into a dict
department_financials_eada_role_dict = department_financials_eada_role_instance.to_dict()
# create an instance of DepartmentFinancialsEadaRole from a dict
department_financials_eada_role_from_dict = DepartmentFinancialsEadaRole.from_dict(department_financials_eada_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


