# PersonAssignment

One position in a person summary (WINAD-10522). Lists are ranked by the lowest non-null position-type ord (unranked last), then sport name, school name, title and position ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **int** |  | 
**year** | **int** | Position season, expressed as its ending year | 
**school_id** | **int** |  | 
**school_name** | **str** |  | 
**school_short_name** | **str** |  | 
**sport_id** | **int** |  | 
**sport_name** | **str** | Sport display name | 
**title** | **str** | Free-text title, otherwise the position-type labels joined with commas | 

## Example

```python
from winthrop_client_python.models.person_assignment import PersonAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of PersonAssignment from a JSON string
person_assignment_instance = PersonAssignment.from_json(json)
# print the JSON string representation of the object
print(PersonAssignment.to_json())

# convert the object into a dict
person_assignment_dict = person_assignment_instance.to_dict()
# create an instance of PersonAssignment from a dict
person_assignment_from_dict = PersonAssignment.from_dict(person_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


