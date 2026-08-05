# DepartmentOverviewDollarShares


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_cents** | **int** |  | 
**lines** | [**List[DepartmentOverviewShareLine]**](DepartmentOverviewShareLine.md) |  | 

## Example

```python
from winthrop_client_python.models.department_overview_dollar_shares import DepartmentOverviewDollarShares

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewDollarShares from a JSON string
department_overview_dollar_shares_instance = DepartmentOverviewDollarShares.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewDollarShares.to_json())

# convert the object into a dict
department_overview_dollar_shares_dict = department_overview_dollar_shares_instance.to_dict()
# create an instance of DepartmentOverviewDollarShares from a dict
department_overview_dollar_shares_from_dict = DepartmentOverviewDollarShares.from_dict(department_overview_dollar_shares_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


