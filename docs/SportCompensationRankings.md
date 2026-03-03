# SportCompensationRankings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_football** | **bool** |  | [optional] 
**years** | **List[int]** |  | [optional] 
**schools** | [**List[SportCompensationRankingsSchoolsInner]**](SportCompensationRankingsSchoolsInner.md) |  | [optional] 
**conference_avgs** | **Dict[str, Optional[float]]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.sport_compensation_rankings import SportCompensationRankings

# TODO update the JSON string below
json = "{}"
# create an instance of SportCompensationRankings from a JSON string
sport_compensation_rankings_instance = SportCompensationRankings.from_json(json)
# print the JSON string representation of the object
print(SportCompensationRankings.to_json())

# convert the object into a dict
sport_compensation_rankings_dict = sport_compensation_rankings_instance.to_dict()
# create an instance of SportCompensationRankings from a dict
sport_compensation_rankings_from_dict = SportCompensationRankings.from_dict(sport_compensation_rankings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


