# PositionSportStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**gender_code** | **str** |  | [optional] 
**high_position_num** | **float** |  | [optional] 
**low_position_num** | **float** |  | [optional] 
**median_position_num** | **float** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.position_sport_stat import PositionSportStat

# TODO update the JSON string below
json = "{}"
# create an instance of PositionSportStat from a JSON string
position_sport_stat_instance = PositionSportStat.from_json(json)
# print the JSON string representation of the object
print(PositionSportStat.to_json())

# convert the object into a dict
position_sport_stat_dict = position_sport_stat_instance.to_dict()
# create an instance of PositionSportStat from a dict
position_sport_stat_from_dict = PositionSportStat.from_dict(position_sport_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


