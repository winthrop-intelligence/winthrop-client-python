# SchoolNoSeason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_no_season import SchoolNoSeason

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolNoSeason from a JSON string
school_no_season_instance = SchoolNoSeason.from_json(json)
# print the JSON string representation of the object
print(SchoolNoSeason.to_json())

# convert the object into a dict
school_no_season_dict = school_no_season_instance.to_dict()
# create an instance of SchoolNoSeason from a dict
school_no_season_from_dict = SchoolNoSeason.from_dict(school_no_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


