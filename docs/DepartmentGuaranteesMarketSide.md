# DepartmentGuaranteesMarketSide


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**your_median_cents** | **int** |  | 
**market_median_cents** | **int** |  | 
**market_count** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_guarantees_market_side import DepartmentGuaranteesMarketSide

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGuaranteesMarketSide from a JSON string
department_guarantees_market_side_instance = DepartmentGuaranteesMarketSide.from_json(json)
# print the JSON string representation of the object
print(DepartmentGuaranteesMarketSide.to_json())

# convert the object into a dict
department_guarantees_market_side_dict = department_guarantees_market_side_instance.to_dict()
# create an instance of DepartmentGuaranteesMarketSide from a dict
department_guarantees_market_side_from_dict = DepartmentGuaranteesMarketSide.from_dict(department_guarantees_market_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


