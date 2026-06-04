# GadCohortSummary

NCAA cohort median / mean / min / max / count benchmark. Returned only when include_cohort_summary=true and sport is provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport** | [**GadSchoolSummarySport**](GadSchoolSummarySport.md) |  | [optional] 
**buyer_cohort** | **str** |  | [optional] 
**seller_cohort** | **str** |  | [optional] 
**buyer_filters** | [**GadCohortSummaryBuyerFilters**](GadCohortSummaryBuyerFilters.md) |  | [optional] 
**seller_filters** | [**GadCohortSummarySellerFilters**](GadCohortSummarySellerFilters.md) |  | [optional] 
**season_window** | **str** |  | [optional] 
**season_filter_applied** | **str** | Year or year-range string actually applied to the underlying query. | [optional] 
**median_amount_cents** | **int** | Median comp_cents across the filtered cohort, excluding comp_tbd&#x3D;true agreements. | [optional] 
**mean_amount_cents** | **int** | Mean comp_cents across the filtered cohort, excluding comp_tbd&#x3D;true agreements. | [optional] 
**min_amount_cents** | **int** |  | [optional] 
**max_amount_cents** | **int** |  | [optional] 
**total_amount_cents** | **int** | Sum of comp_cents across the filtered cohort, excluding comp_tbd&#x3D;true agreements. Counts still include TBD agreements. | [optional] 
**agreement_count** | **int** |  | [optional] 
**permission_filtered_count** | **int** | Unfiltered count minus accessible_by-filtered count at the same predicate set. | [optional] 
**source_updated_at** | **datetime** | Max updated_at across the rows included in the cohort summary. | [optional] 
**caveats** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.gad_cohort_summary import GadCohortSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GadCohortSummary from a JSON string
gad_cohort_summary_instance = GadCohortSummary.from_json(json)
# print the JSON string representation of the object
print(GadCohortSummary.to_json())

# convert the object into a dict
gad_cohort_summary_dict = gad_cohort_summary_instance.to_dict()
# create an instance of GadCohortSummary from a dict
gad_cohort_summary_from_dict = GadCohortSummary.from_dict(gad_cohort_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


