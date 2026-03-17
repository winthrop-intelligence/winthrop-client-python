# ComparisonSectionCoachesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_friendly_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**school** | **str** |  | [optional] 
**school_id** | **int** |  | [optional] 
**comp_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.comparison_section_coaches_inner import ComparisonSectionCoachesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ComparisonSectionCoachesInner from a JSON string
comparison_section_coaches_inner_instance = ComparisonSectionCoachesInner.from_json(json)
# print the JSON string representation of the object
print(ComparisonSectionCoachesInner.to_json())

# convert the object into a dict
comparison_section_coaches_inner_dict = comparison_section_coaches_inner_instance.to_dict()
# create an instance of ComparisonSectionCoachesInner from a dict
comparison_section_coaches_inner_from_dict = ComparisonSectionCoachesInner.from_dict(comparison_section_coaches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


