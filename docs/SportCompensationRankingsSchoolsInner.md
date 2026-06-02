# SportCompensationRankingsSchoolsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**avg** | **float** |  | [optional] 
**net_avg** | **float** |  | [optional] 
**by_year** | **Dict[str, Optional[float]]** | Primary ranking values by year. For football this is AP rank; otherwise this is RPI. | [optional] 
**net_by_year** | **Dict[str, Optional[float]]** | NET ranking values by year for non-football sports. | [optional] 
**ap_by_year** | **Dict[str, Optional[float]]** | AP ranking values by year for football. | [optional] 

## Example

```python
from winthrop_client_python.models.sport_compensation_rankings_schools_inner import SportCompensationRankingsSchoolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SportCompensationRankingsSchoolsInner from a JSON string
sport_compensation_rankings_schools_inner_instance = SportCompensationRankingsSchoolsInner.from_json(json)
# print the JSON string representation of the object
print(SportCompensationRankingsSchoolsInner.to_json())

# convert the object into a dict
sport_compensation_rankings_schools_inner_dict = sport_compensation_rankings_schools_inner_instance.to_dict()
# create an instance of SportCompensationRankingsSchoolsInner from a dict
sport_compensation_rankings_schools_inner_from_dict = SportCompensationRankingsSchoolsInner.from_dict(sport_compensation_rankings_schools_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


