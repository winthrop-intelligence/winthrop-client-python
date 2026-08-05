# AthleticProfileShowSportFinancialsQuadrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fiscal_year** | **int** |  | [optional] 
**points** | [**List[AthleticProfileShowSportFinancialsQuadrantPointsInner]**](AthleticProfileShowSportFinancialsQuadrantPointsInner.md) |  | [optional] 
**unplotted** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_financials_quadrant import AthleticProfileShowSportFinancialsQuadrant

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportFinancialsQuadrant from a JSON string
athletic_profile_show_sport_financials_quadrant_instance = AthleticProfileShowSportFinancialsQuadrant.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportFinancialsQuadrant.to_json())

# convert the object into a dict
athletic_profile_show_sport_financials_quadrant_dict = athletic_profile_show_sport_financials_quadrant_instance.to_dict()
# create an instance of AthleticProfileShowSportFinancialsQuadrant from a dict
athletic_profile_show_sport_financials_quadrant_from_dict = AthleticProfileShowSportFinancialsQuadrant.from_dict(athletic_profile_show_sport_financials_quadrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


