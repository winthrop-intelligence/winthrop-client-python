# DirectorsCupSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**rankings** | **Dict[str, Optional[int]]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.directors_cup_school import DirectorsCupSchool

# TODO update the JSON string below
json = "{}"
# create an instance of DirectorsCupSchool from a JSON string
directors_cup_school_instance = DirectorsCupSchool.from_json(json)
# print the JSON string representation of the object
print(DirectorsCupSchool.to_json())

# convert the object into a dict
directors_cup_school_dict = directors_cup_school_instance.to_dict()
# create an instance of DirectorsCupSchool from a dict
directors_cup_school_from_dict = DirectorsCupSchool.from_dict(directors_cup_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


