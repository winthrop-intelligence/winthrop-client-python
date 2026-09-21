# AthleticProfileShowSportFinancialsQuadrantPointsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**colors** | **str** |  | [optional] 
**is_subject** | **bool** |  | [optional] 
**spend_cents** | **int** |  | [optional] 
**revenue_cents** | **int** |  | [optional] 
**basis** | **str** | Which report this program&#39;s money was read from. Private peers with no FRS sport filing plot from their federal EADA sport row — a separate report with different definitions, so the page marks these points rather than presenting the two bases as one filing (WINAD-10385). | [optional] 
**basis_year** | **int** | EADA reporting year the figures came from (may differ from the quadrant&#39;s FRS fiscal_year). Null for FRS points. | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_financials_quadrant_points_inner import AthleticProfileShowSportFinancialsQuadrantPointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportFinancialsQuadrantPointsInner from a JSON string
athletic_profile_show_sport_financials_quadrant_points_inner_instance = AthleticProfileShowSportFinancialsQuadrantPointsInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportFinancialsQuadrantPointsInner.to_json())

# convert the object into a dict
athletic_profile_show_sport_financials_quadrant_points_inner_dict = athletic_profile_show_sport_financials_quadrant_points_inner_instance.to_dict()
# create an instance of AthleticProfileShowSportFinancialsQuadrantPointsInner from a dict
athletic_profile_show_sport_financials_quadrant_points_inner_from_dict = AthleticProfileShowSportFinancialsQuadrantPointsInner.from_dict(athletic_profile_show_sport_financials_quadrant_points_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


