# AthleticProfileShowSportOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**results_lens** | **str** | The results metric this surface is read through, resolved per season from the sport&#39;s rank chain (NET → RPI for basketball, RPI otherwise) with CONF_WINS as the fallback when no rank is filed (WINAD-10259). Metric fields ship for every column; the lens names the one a surface may claim. | [optional] 
**seasons** | [**List[AthleticProfileShowSportOverviewSeasonsInner]**](AthleticProfileShowSportOverviewSeasonsInner.md) |  | [optional] 
**head_coach** | [**AthleticProfileShowSportOverviewHeadCoach**](AthleticProfileShowSportOverviewHeadCoach.md) |  | [optional] 
**pay_ladder** | [**List[AthleticProfileShowSportOverviewPayLadderInner]**](AthleticProfileShowSportOverviewPayLadderInner.md) |  | [optional] 
**quadrant_points** | [**List[AthleticProfileShowSportOverviewQuadrantPointsInner]**](AthleticProfileShowSportOverviewQuadrantPointsInner.md) |  | [optional] 
**guarantees** | [**AthleticProfileShowSportOverviewGuarantees**](AthleticProfileShowSportOverviewGuarantees.md) |  | [optional] 
**as_of** | **date** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_overview import AthleticProfileShowSportOverview

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportOverview from a JSON string
athletic_profile_show_sport_overview_instance = AthleticProfileShowSportOverview.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportOverview.to_json())

# convert the object into a dict
athletic_profile_show_sport_overview_dict = athletic_profile_show_sport_overview_instance.to_dict()
# create an instance of AthleticProfileShowSportOverview from a dict
athletic_profile_show_sport_overview_from_dict = AthleticProfileShowSportOverview.from_dict(athletic_profile_show_sport_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


