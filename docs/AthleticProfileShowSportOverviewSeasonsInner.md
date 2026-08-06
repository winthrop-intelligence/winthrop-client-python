# AthleticProfileShowSportOverviewSeasonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**record** | **str** |  | [optional] 
**conference_record** | **str** |  | [optional] 
**net_rank** | **int** |  | [optional] 
**postseason** | **str** |  | [optional] 
**head_coach_name** | **str** |  | [optional] 
**head_coach_interim** | **bool** | True when the season&#39;s seat-holder is filed only as INTERIM_HEAD_COACH. | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_overview_seasons_inner import AthleticProfileShowSportOverviewSeasonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportOverviewSeasonsInner from a JSON string
athletic_profile_show_sport_overview_seasons_inner_instance = AthleticProfileShowSportOverviewSeasonsInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportOverviewSeasonsInner.to_json())

# convert the object into a dict
athletic_profile_show_sport_overview_seasons_inner_dict = athletic_profile_show_sport_overview_seasons_inner_instance.to_dict()
# create an instance of AthleticProfileShowSportOverviewSeasonsInner from a dict
athletic_profile_show_sport_overview_seasons_inner_from_dict = AthleticProfileShowSportOverviewSeasonsInner.from_dict(athletic_profile_show_sport_overview_seasons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


