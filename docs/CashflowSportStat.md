# CashflowSportStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**gender_code** | **str** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**median** | **float** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.cashflow_sport_stat import CashflowSportStat

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowSportStat from a JSON string
cashflow_sport_stat_instance = CashflowSportStat.from_json(json)
# print the JSON string representation of the object
print(CashflowSportStat.to_json())

# convert the object into a dict
cashflow_sport_stat_dict = cashflow_sport_stat_instance.to_dict()
# create an instance of CashflowSportStat from a dict
cashflow_sport_stat_from_dict = CashflowSportStat.from_dict(cashflow_sport_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


