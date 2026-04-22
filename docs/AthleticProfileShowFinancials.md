# AthleticProfileShowFinancials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**years** | **List[int]** |  | [optional] 
**revenues** | [**List[AthleticProfileShowFinancialsRevenuesInner]**](AthleticProfileShowFinancialsRevenuesInner.md) |  | [optional] 
**expenses** | [**List[AthleticProfileShowFinancialsRevenuesInner]**](AthleticProfileShowFinancialsRevenuesInner.md) |  | [optional] 
**chart_revenues** | **List[float]** |  | [optional] 
**chart_expenses** | **List[float]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_financials import AthleticProfileShowFinancials

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowFinancials from a JSON string
athletic_profile_show_financials_instance = AthleticProfileShowFinancials.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowFinancials.to_json())

# convert the object into a dict
athletic_profile_show_financials_dict = athletic_profile_show_financials_instance.to_dict()
# create an instance of AthleticProfileShowFinancials from a dict
athletic_profile_show_financials_from_dict = AthleticProfileShowFinancials.from_dict(athletic_profile_show_financials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


