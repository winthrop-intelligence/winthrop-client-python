# AdminPlayerStatFilterOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schools** | [**List[IdName]**](IdName.md) |  | [optional] 
**current_season_year** | **int** | SystemSetting.current_season_year | [optional] 
**year_options** | [**List[AdminPlayerStatFilterOptionsYearOptionsInner]**](AdminPlayerStatFilterOptionsYearOptionsInner.md) | The search form&#39;s Year select (2 years forward, 6 back from the current season) | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_stat_filter_options import AdminPlayerStatFilterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerStatFilterOptions from a JSON string
admin_player_stat_filter_options_instance = AdminPlayerStatFilterOptions.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerStatFilterOptions.to_json())

# convert the object into a dict
admin_player_stat_filter_options_dict = admin_player_stat_filter_options_instance.to_dict()
# create an instance of AdminPlayerStatFilterOptions from a dict
admin_player_stat_filter_options_from_dict = AdminPlayerStatFilterOptions.from_dict(admin_player_stat_filter_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


