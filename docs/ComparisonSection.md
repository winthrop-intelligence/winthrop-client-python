# ComparisonSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | 
**coaches** | [**List[ComparisonSectionCoachesInner]**](ComparisonSectionCoachesInner.md) |  | 

## Example

```python
from winthrop_client_python.models.comparison_section import ComparisonSection

# TODO update the JSON string below
json = "{}"
# create an instance of ComparisonSection from a JSON string
comparison_section_instance = ComparisonSection.from_json(json)
# print the JSON string representation of the object
print(ComparisonSection.to_json())

# convert the object into a dict
comparison_section_dict = comparison_section_instance.to_dict()
# create an instance of ComparisonSection from a dict
comparison_section_from_dict = ComparisonSection.from_dict(comparison_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


