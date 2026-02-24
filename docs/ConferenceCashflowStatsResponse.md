# ConferenceCashflowStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**groups** | [**List[CashflowGroupStats]**](CashflowGroupStats.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.conference_cashflow_stats_response import ConferenceCashflowStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceCashflowStatsResponse from a JSON string
conference_cashflow_stats_response_instance = ConferenceCashflowStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ConferenceCashflowStatsResponse.to_json())

# convert the object into a dict
conference_cashflow_stats_response_dict = conference_cashflow_stats_response_instance.to_dict()
# create an instance of ConferenceCashflowStatsResponse from a dict
conference_cashflow_stats_response_from_dict = ConferenceCashflowStatsResponse.from_dict(conference_cashflow_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


