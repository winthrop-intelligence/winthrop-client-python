# DepartmentOverviewPrivateDisclosure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_class** | [**List[DepartmentOverviewPrivateDisclosureLine]**](DepartmentOverviewPrivateDisclosureLine.md) |  | 
**degrades** | [**List[DepartmentOverviewPrivateDisclosureLine]**](DepartmentOverviewPrivateDisclosureLine.md) |  | 

## Example

```python
from winthrop_client_python.models.department_overview_private_disclosure import DepartmentOverviewPrivateDisclosure

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateDisclosure from a JSON string
department_overview_private_disclosure_instance = DepartmentOverviewPrivateDisclosure.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateDisclosure.to_json())

# convert the object into a dict
department_overview_private_disclosure_dict = department_overview_private_disclosure_instance.to_dict()
# create an instance of DepartmentOverviewPrivateDisclosure from a dict
department_overview_private_disclosure_from_dict = DepartmentOverviewPrivateDisclosure.from_dict(department_overview_private_disclosure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


