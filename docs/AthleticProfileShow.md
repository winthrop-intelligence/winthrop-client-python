# AthleticProfileShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**AthleticProfileShowSchool**](AthleticProfileShowSchool.md) |  | [optional] 
**financial_info** | [**AthleticProfileShowFinancialInfo**](AthleticProfileShowFinancialInfo.md) |  | [optional] 
**sport_key** | **str** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**tab_sports** | [**List[AthleticProfileShowTabSportsInner]**](AthleticProfileShowTabSportsInner.md) |  | [optional] 
**non_revenue_sports** | [**List[AthleticProfileShowTabSportsInner]**](AthleticProfileShowTabSportsInner.md) |  | [optional] 
**permissions** | [**AthleticProfileShowPermissions**](AthleticProfileShowPermissions.md) |  | [optional] 
**sports_overview** | [**List[AthleticProfileShowSportsOverviewInner]**](AthleticProfileShowSportsOverviewInner.md) |  | [optional] 
**sponsored_count** | **int** |  | [optional] 
**personnel** | [**List[AthleticProfileShowPersonnelInner]**](AthleticProfileShowPersonnelInner.md) |  | [optional] 
**personnel_total_count** | **int** |  | [optional] 
**financials** | [**AthleticProfileShowFinancials**](AthleticProfileShowFinancials.md) |  | [optional] 
**deals** | [**List[AthleticProfileShowDealsInner]**](AthleticProfileShowDealsInner.md) |  | [optional] 
**guarantees** | [**List[AthleticProfileShowGuaranteesInner]**](AthleticProfileShowGuaranteesInner.md) |  | [optional] 
**guarantees_total_count** | **int** |  | [optional] 
**games** | [**List[AthleticProfileShowGamesInner]**](AthleticProfileShowGamesInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show import AthleticProfileShow

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShow from a JSON string
athletic_profile_show_instance = AthleticProfileShow.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShow.to_json())

# convert the object into a dict
athletic_profile_show_dict = athletic_profile_show_instance.to_dict()
# create an instance of AthleticProfileShow from a dict
athletic_profile_show_from_dict = AthleticProfileShow.from_dict(athletic_profile_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


