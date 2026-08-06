# DepartmentCoachesPortfolioShape


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outperforming** | [**DepartmentCoachesShapeEntry**](DepartmentCoachesShapeEntry.md) |  | 
**in_line** | [**DepartmentCoachesShapeEntry**](DepartmentCoachesShapeEntry.md) |  | 
**underdelivering** | [**DepartmentCoachesShapeEntry**](DepartmentCoachesShapeEntry.md) |  | 

## Example

```python
from winthrop_client_python.models.department_coaches_portfolio_shape import DepartmentCoachesPortfolioShape

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachesPortfolioShape from a JSON string
department_coaches_portfolio_shape_instance = DepartmentCoachesPortfolioShape.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachesPortfolioShape.to_json())

# convert the object into a dict
department_coaches_portfolio_shape_dict = department_coaches_portfolio_shape_instance.to_dict()
# create an instance of DepartmentCoachesPortfolioShape from a dict
department_coaches_portfolio_shape_from_dict = DepartmentCoachesPortfolioShape.from_dict(department_coaches_portfolio_shape_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


