# DepartmentGuaranteesMarket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window** | **str** |  | 
**seasons** | **List[int]** |  | 
**football** | [**DepartmentGuaranteesMarketSide**](DepartmentGuaranteesMarketSide.md) |  | 
**mens_basketball** | [**DepartmentGuaranteesMarketSide**](DepartmentGuaranteesMarketSide.md) |  | 

## Example

```python
from winthrop_client_python.models.department_guarantees_market import DepartmentGuaranteesMarket

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGuaranteesMarket from a JSON string
department_guarantees_market_instance = DepartmentGuaranteesMarket.from_json(json)
# print the JSON string representation of the object
print(DepartmentGuaranteesMarket.to_json())

# convert the object into a dict
department_guarantees_market_dict = department_guarantees_market_instance.to_dict()
# create an instance of DepartmentGuaranteesMarket from a dict
department_guarantees_market_from_dict = DepartmentGuaranteesMarket.from_dict(department_guarantees_market_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


