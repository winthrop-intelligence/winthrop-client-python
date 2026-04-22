# AthleticProfileShowSportsOverviewInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_name** | **str** |  | [optional] 
**sport_key** | **str** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**head_coach_name** | **str** |  | [optional] 
**head_coach_id** | **int** |  | [optional] 
**record** | **str** |  | [optional] 
**apr** | **int** |  | [optional] 
**rpi** | **int** |  | [optional] 
**head_coach_comp_cents** | **int** |  | [optional] 
**asst_pool_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sports_overview_inner import AthleticProfileShowSportsOverviewInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportsOverviewInner from a JSON string
athletic_profile_show_sports_overview_inner_instance = AthleticProfileShowSportsOverviewInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportsOverviewInner.to_json())

# convert the object into a dict
athletic_profile_show_sports_overview_inner_dict = athletic_profile_show_sports_overview_inner_instance.to_dict()
# create an instance of AthleticProfileShowSportsOverviewInner from a dict
athletic_profile_show_sports_overview_inner_from_dict = AthleticProfileShowSportsOverviewInner.from_dict(athletic_profile_show_sports_overview_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


