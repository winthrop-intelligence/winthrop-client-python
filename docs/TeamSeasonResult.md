# TeamSeasonResult

One result of a team's season (WINAD-10636), shared by every coach of that team. school_id, sport_id and season_year come from the season row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**season_id** | **int** |  | 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**season_year** | **int** | Season end year (2023 &#x3D; the 2022-23 season). | [optional] 
**result_name** | **str** |  | 
**result_value** | **str** | Null while the result is unresolved; each lane&#39;s value then sits in details. | [optional] 
**details** | **Dict[str, object]** |  | [optional] 
**source_url** | **str** |  | [optional] 
**quote** | **str** |  | [optional] 
**season_anchor** | **str** |  | [optional] 
**verification_method** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_season_result import TeamSeasonResult

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonResult from a JSON string
team_season_result_instance = TeamSeasonResult.from_json(json)
# print the JSON string representation of the object
print(TeamSeasonResult.to_json())

# convert the object into a dict
team_season_result_dict = team_season_result_instance.to_dict()
# create an instance of TeamSeasonResult from a dict
team_season_result_from_dict = TeamSeasonResult.from_dict(team_season_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


