# DepartmentCoachesShapeEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**approximate** | **bool** |  | 
**sport_abbrevs** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.department_coaches_shape_entry import DepartmentCoachesShapeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachesShapeEntry from a JSON string
department_coaches_shape_entry_instance = DepartmentCoachesShapeEntry.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachesShapeEntry.to_json())

# convert the object into a dict
department_coaches_shape_entry_dict = department_coaches_shape_entry_instance.to_dict()
# create an instance of DepartmentCoachesShapeEntry from a dict
department_coaches_shape_entry_from_dict = DepartmentCoachesShapeEntry.from_dict(department_coaches_shape_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


