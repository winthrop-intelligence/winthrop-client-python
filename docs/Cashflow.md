# Cashflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**season_id** | **int** |  | [optional] 
**cashflow_group_id** | **int** |  | [optional] 
**amount** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.cashflow import Cashflow

# TODO update the JSON string below
json = "{}"
# create an instance of Cashflow from a JSON string
cashflow_instance = Cashflow.from_json(json)
# print the JSON string representation of the object
print(Cashflow.to_json())

# convert the object into a dict
cashflow_dict = cashflow_instance.to_dict()
# create an instance of Cashflow from a dict
cashflow_from_dict = Cashflow.from_dict(cashflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


