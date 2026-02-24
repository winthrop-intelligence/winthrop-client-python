# SportCompensationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**compensations** | [**List[CompensationRow]**](CompensationRow.md) |  | [optional] 
**schools_no_comp** | [**List[SchoolNoComp]**](SchoolNoComp.md) |  | [optional] 
**schools_no_season** | [**List[SchoolNoSeason]**](SchoolNoSeason.md) |  | [optional] 
**assistant_coaches** | [**List[AsstCoachSchool]**](AsstCoachSchool.md) |  | [optional] 
**subdivisions** | [**List[SportCompensationSubdivision]**](SportCompensationSubdivision.md) |  | [optional] 
**rankings** | [**SportCompensationRankings**](SportCompensationRankings.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.sport_compensation_response import SportCompensationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SportCompensationResponse from a JSON string
sport_compensation_response_instance = SportCompensationResponse.from_json(json)
# print the JSON string representation of the object
print(SportCompensationResponse.to_json())

# convert the object into a dict
sport_compensation_response_dict = sport_compensation_response_instance.to_dict()
# create an instance of SportCompensationResponse from a dict
sport_compensation_response_from_dict = SportCompensationResponse.from_dict(sport_compensation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


