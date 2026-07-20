# CompensationComparisonCohortStats

Stats cover the full pre-cap candidate set; min/median/max/average are computed over rows with comp_status=included only, and denominator_rule spells out every exclusion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included_count** | **int** |  | 
**no_role_match_count** | **int** |  | 
**school_not_accessible_count** | **int** |  | 
**missing_compensation_count** | **int** |  | 
**zero_or_volunteer_count** | **int** |  | 
**comp_redacted_count** | **int** |  | 
**match_type_counts** | **Dict[str, int]** |  | 
**min_cents** | **int** |  | 
**max_cents** | **int** |  | 
**average_cents** | **int** |  | 
**median_cents** | **int** |  | 
**denominator_rule** | **str** |  | 

## Example

```python
from winthrop_client_python.models.compensation_comparison_cohort_stats import CompensationComparisonCohortStats

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationComparisonCohortStats from a JSON string
compensation_comparison_cohort_stats_instance = CompensationComparisonCohortStats.from_json(json)
# print the JSON string representation of the object
print(CompensationComparisonCohortStats.to_json())

# convert the object into a dict
compensation_comparison_cohort_stats_dict = compensation_comparison_cohort_stats_instance.to_dict()
# create an instance of CompensationComparisonCohortStats from a dict
compensation_comparison_cohort_stats_from_dict = CompensationComparisonCohortStats.from_dict(compensation_comparison_cohort_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


