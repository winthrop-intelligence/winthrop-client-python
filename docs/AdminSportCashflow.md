# AdminSportCashflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**school_id** | **int** |  | 
**school_name** | **str** |  | 
**year** | **int** |  | 
**cashflow_group_id** | **int** |  | 
**cashflow_group_name** | **str** |  | 
**amount** | **int** | Amount in cents | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.admin_sport_cashflow import AdminSportCashflow

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSportCashflow from a JSON string
admin_sport_cashflow_instance = AdminSportCashflow.from_json(json)
# print the JSON string representation of the object
print(AdminSportCashflow.to_json())

# convert the object into a dict
admin_sport_cashflow_dict = admin_sport_cashflow_instance.to_dict()
# create an instance of AdminSportCashflow from a dict
admin_sport_cashflow_from_dict = AdminSportCashflow.from_dict(admin_sport_cashflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


