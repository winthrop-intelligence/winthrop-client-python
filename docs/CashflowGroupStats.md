# CashflowGroupStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** |  | [optional] 
**name_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**sports** | [**List[CashflowSportStat]**](CashflowSportStat.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.cashflow_group_stats import CashflowGroupStats

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowGroupStats from a JSON string
cashflow_group_stats_instance = CashflowGroupStats.from_json(json)
# print the JSON string representation of the object
print(CashflowGroupStats.to_json())

# convert the object into a dict
cashflow_group_stats_dict = cashflow_group_stats_instance.to_dict()
# create an instance of CashflowGroupStats from a dict
cashflow_group_stats_from_dict = CashflowGroupStats.from_dict(cashflow_group_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


