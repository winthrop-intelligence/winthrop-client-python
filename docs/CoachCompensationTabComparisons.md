# CoachCompensationTabComparisons


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference** | [**ComparisonSection**](ComparisonSection.md) |  | [optional] 
**division** | [**ComparisonSection**](ComparisonSection.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_compensation_tab_comparisons import CoachCompensationTabComparisons

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensationTabComparisons from a JSON string
coach_compensation_tab_comparisons_instance = CoachCompensationTabComparisons.from_json(json)
# print the JSON string representation of the object
print(CoachCompensationTabComparisons.to_json())

# convert the object into a dict
coach_compensation_tab_comparisons_dict = coach_compensation_tab_comparisons_instance.to_dict()
# create an instance of CoachCompensationTabComparisons from a dict
coach_compensation_tab_comparisons_from_dict = CoachCompensationTabComparisons.from_dict(coach_compensation_tab_comparisons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


