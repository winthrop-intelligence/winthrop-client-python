# SchoolInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_student_enrollment** | **int** |  | [optional] 
**male_students** | **int** |  | [optional] 
**female_students** | **int** |  | [optional] 
**student_athlete_enrollment** | **int** |  | [optional] 
**male_athletes** | **int** |  | [optional] 
**female_athletes** | **int** |  | [optional] 
**sport_count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_info import SchoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolInfo from a JSON string
school_info_instance = SchoolInfo.from_json(json)
# print the JSON string representation of the object
print(SchoolInfo.to_json())

# convert the object into a dict
school_info_dict = school_info_instance.to_dict()
# create an instance of SchoolInfo from a dict
school_info_from_dict = SchoolInfo.from_dict(school_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


