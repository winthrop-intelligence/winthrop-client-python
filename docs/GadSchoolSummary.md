# GadSchoolSummary

Per-school median / mean / min / max / count over the requested season window. Returned only when include_school_summary=true and inputs are valid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**GadSchoolSummarySchool**](GadSchoolSummarySchool.md) |  | [optional] 
**sport** | [**GadSchoolSummarySport**](GadSchoolSummarySport.md) |  | [optional] 
**season_window** | **str** | One of last_3_completed_seasons | specific_year | custom_range. | [optional] 
**included_seasons** | **List[int]** | Distinct season_year values present in the filtered scope. | [optional] 
**median_paid_out_cents** | **int** | Median comp_cents across paid_out rows, excluding comp_tbd&#x3D;true agreements. | [optional] 
**median_received_cents** | **int** | Median comp_cents across received rows, excluding comp_tbd&#x3D;true agreements. | [optional] 
**mean_paid_out_cents** | **int** | Mean comp_cents across paid_out rows, excluding comp_tbd&#x3D;true agreements. | [optional] 
**mean_received_cents** | **int** | Mean comp_cents across received rows, excluding comp_tbd&#x3D;true agreements. | [optional] 
**min_paid_out_cents** | **int** |  | [optional] 
**max_paid_out_cents** | **int** |  | [optional] 
**min_received_cents** | **int** |  | [optional] 
**max_received_cents** | **int** |  | [optional] 
**total_paid_out_cents** | **int** | Sum of comp_cents across paid_out (home-side) rows, excluding comp_tbd&#x3D;true agreements. Counts still include TBD agreements. | [optional] 
**total_received_cents** | **int** | Sum of comp_cents across received (away-side) rows, excluding comp_tbd&#x3D;true agreements. Counts still include TBD agreements. | [optional] 
**paid_out_agreement_count** | **int** |  | [optional] 
**received_agreement_count** | **int** |  | [optional] 
**permission_filtered_count** | **int** | Count of agreements the caller cannot see due to ability filtering — unfiltered count minus accessible_by-filtered count at the same predicate set. | [optional] 
**source_updated_at** | **datetime** | Max updated_at across the rows included in the summary. | [optional] 
**caveats** | **List[str]** | Free-text caveats about the summary (e.g. excluded TBD comp, variable comp, small sample). | [optional] 

## Example

```python
from winthrop_client_python.models.gad_school_summary import GadSchoolSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GadSchoolSummary from a JSON string
gad_school_summary_instance = GadSchoolSummary.from_json(json)
# print the JSON string representation of the object
print(GadSchoolSummary.to_json())

# convert the object into a dict
gad_school_summary_dict = gad_school_summary_instance.to_dict()
# create an instance of GadSchoolSummary from a dict
gad_school_summary_from_dict = GadSchoolSummary.from_dict(gad_school_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


