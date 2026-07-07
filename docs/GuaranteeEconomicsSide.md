# GuaranteeEconomicsSide

One side (host = school paid as home team; travel = school was paid as visitor) of the guarantee economics. Null when there are no qualifying money games in the window or the caller lacks guarantee aggregate access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**median_cents** | **int** | Median guarantee in cents across qualifying money games (game_type Guarantee, comp_cents &gt; 0, comp_tbd false). | [optional] 
**count** | **int** | Number of money games behind the median (sample size N). | [optional] 
**gad_filters** | **Dict[str, object]** | Ransack params for /gad_searches reproducing exactly the games behind the median — the Guarantees-tab deep-link target (sport_id_eq, home_school_id_eq or away_school_id_eq, game_type_eq, season_year_in). | [optional] 

## Example

```python
from winthrop_client_python.models.guarantee_economics_side import GuaranteeEconomicsSide

# TODO update the JSON string below
json = "{}"
# create an instance of GuaranteeEconomicsSide from a JSON string
guarantee_economics_side_instance = GuaranteeEconomicsSide.from_json(json)
# print the JSON string representation of the object
print(GuaranteeEconomicsSide.to_json())

# convert the object into a dict
guarantee_economics_side_dict = guarantee_economics_side_instance.to_dict()
# create an instance of GuaranteeEconomicsSide from a dict
guarantee_economics_side_from_dict = GuaranteeEconomicsSide.from_dict(guarantee_economics_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


