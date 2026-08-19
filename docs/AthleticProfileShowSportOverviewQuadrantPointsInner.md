# AthleticProfileShowSportOverviewQuadrantPointsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**colors** | **str** |  | [optional] 
**is_subject** | **bool** |  | [optional] 
**spend_cents** | **int** |  | [optional] 
**spend_year** | **int** |  | [optional] 
**net_rank** | **int** |  | [optional] 
**rpi** | **int** |  | [optional] 
**conference_wins** | **int** |  | [optional] 
**record** | **str** | Overall record for the season the point plots (results_year), null when that season filed none. | [optional] 
**conference_record** | **str** | Conference record for the season the point plots — the pair a conference-wins value is read against (WINAD-10268). Null when that season filed none. | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_overview_quadrant_points_inner import AthleticProfileShowSportOverviewQuadrantPointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportOverviewQuadrantPointsInner from a JSON string
athletic_profile_show_sport_overview_quadrant_points_inner_instance = AthleticProfileShowSportOverviewQuadrantPointsInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportOverviewQuadrantPointsInner.to_json())

# convert the object into a dict
athletic_profile_show_sport_overview_quadrant_points_inner_dict = athletic_profile_show_sport_overview_quadrant_points_inner_instance.to_dict()
# create an instance of AthleticProfileShowSportOverviewQuadrantPointsInner from a dict
athletic_profile_show_sport_overview_quadrant_points_inner_from_dict = AthleticProfileShowSportOverviewQuadrantPointsInner.from_dict(athletic_profile_show_sport_overview_quadrant_points_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


