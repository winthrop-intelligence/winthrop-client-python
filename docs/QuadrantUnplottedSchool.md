# QuadrantUnplottedSchool

A cohort member a quadrant cannot plot, and why — shared by the Cup-vs-spend quadrants (dept Administrators; the Overview hero predates this schema and keeps its own identical shape)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**name** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from winthrop_client_python.models.quadrant_unplotted_school import QuadrantUnplottedSchool

# TODO update the JSON string below
json = "{}"
# create an instance of QuadrantUnplottedSchool from a JSON string
quadrant_unplotted_school_instance = QuadrantUnplottedSchool.from_json(json)
# print the JSON string representation of the object
print(QuadrantUnplottedSchool.to_json())

# convert the object into a dict
quadrant_unplotted_school_dict = quadrant_unplotted_school_instance.to_dict()
# create an instance of QuadrantUnplottedSchool from a dict
quadrant_unplotted_school_from_dict = QuadrantUnplottedSchool.from_dict(quadrant_unplotted_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


