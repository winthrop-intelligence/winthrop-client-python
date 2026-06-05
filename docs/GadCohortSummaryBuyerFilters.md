# GadCohortSummaryBuyerFilters

Resolved buyer-side conference/division/subdivision IDs that were applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference_id** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**subdivision_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.gad_cohort_summary_buyer_filters import GadCohortSummaryBuyerFilters

# TODO update the JSON string below
json = "{}"
# create an instance of GadCohortSummaryBuyerFilters from a JSON string
gad_cohort_summary_buyer_filters_instance = GadCohortSummaryBuyerFilters.from_json(json)
# print the JSON string representation of the object
print(GadCohortSummaryBuyerFilters.to_json())

# convert the object into a dict
gad_cohort_summary_buyer_filters_dict = gad_cohort_summary_buyer_filters_instance.to_dict()
# create an instance of GadCohortSummaryBuyerFilters from a dict
gad_cohort_summary_buyer_filters_from_dict = GadCohortSummaryBuyerFilters.from_dict(gad_cohort_summary_buyer_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


