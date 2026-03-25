# SchoolSportSeason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**losses** | **int** |  | [optional] 
**rpi** | **float** |  | [optional] 
**sos** | **float** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_sport_season import SchoolSportSeason

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolSportSeason from a JSON string
school_sport_season_instance = SchoolSportSeason.from_json(json)
# print the JSON string representation of the object
print(SchoolSportSeason.to_json())

# convert the object into a dict
school_sport_season_dict = school_sport_season_instance.to_dict()
# create an instance of SchoolSportSeason from a dict
school_sport_season_from_dict = SchoolSportSeason.from_dict(school_sport_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


