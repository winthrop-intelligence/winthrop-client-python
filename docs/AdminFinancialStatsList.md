# AdminFinancialStatsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminCoachContractsQcListMeta**](AdminCoachContractsQcListMeta.md) |  | [optional] 
**data** | [**List[AdminFinancialStat]**](AdminFinancialStat.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_financial_stats_list import AdminFinancialStatsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFinancialStatsList from a JSON string
admin_financial_stats_list_instance = AdminFinancialStatsList.from_json(json)
# print the JSON string representation of the object
print(AdminFinancialStatsList.to_json())

# convert the object into a dict
admin_financial_stats_list_dict = admin_financial_stats_list_instance.to_dict()
# create an instance of AdminFinancialStatsList from a dict
admin_financial_stats_list_from_dict = AdminFinancialStatsList.from_dict(admin_financial_stats_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


