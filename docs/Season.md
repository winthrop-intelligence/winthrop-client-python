# Season


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**losses** | **int** |  | [optional] 
**conference_wins** | **int** |  | [optional] 
**conference_losses** | **int** |  | [optional] 
**apr** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**win_percent** | **float** |  | [optional] 
**ties** | **int** |  | [optional] 
**rpi** | **int** |  | [optional] 
**prev_rpi** | **int** |  | [optional] 
**conference_position** | **int** |  | [optional] 
**conference_num_positions** | **int** |  | [optional] 
**coach_apr** | **int** |  | [optional] 
**attendance** | **int** |  | [optional] 
**conference_ties** | **int** |  | [optional] 
**recruit_ranking** | **int** |  | [optional] 
**offensive_efficiency** | **float** |  | [optional] 
**defensive_efficiency** | **float** |  | [optional] 
**sos_ranking** | **int** |  | [optional] 
**sos** | **float** |  | [optional] 
**home_wins** | **int** |  | [optional] 
**home_losses** | **int** |  | [optional] 
**home_win_percent** | **float** |  | [optional] 
**asr** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.season import Season

# TODO update the JSON string below
json = "{}"
# create an instance of Season from a JSON string
season_instance = Season.from_json(json)
# print the JSON string representation of the object
print(Season.to_json())

# convert the object into a dict
season_dict = season_instance.to_dict()
# create an instance of Season from a dict
season_from_dict = Season.from_dict(season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


