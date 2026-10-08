# FoiaStatusSummaryMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of_date** | **date** | America/New_York calendar date used for every comparison on every page; must be identical across pages of one collection. Overdue is strictly before this date; follow-up due is on or before it. | 
**generated_at** | **datetime** | RFC 3339 UTC timestamp regenerated per page (with UTC &#39;Z&#39; offset); may differ between pages. | 
**timezone** | **str** | IANA name of the business time zone used for as_of_date (America/New_York). | 
**filters_applied** | [**FoiaStatusSummaryFilters**](FoiaStatusSummaryFilters.md) |  | 
**current_page** | **int** |  | 
**per_page** | **int** | Effective page size after capping the requested value to 200. | 
**max_per_page** | **int** |  | 
**total_pages** | **int** |  | 
**total_entries** | **int** |  | 
**next_page** | **int** |  | 
**previous_page** | **int** |  | 
**active_hold_note_prefix** | **str** |  | 
**active_hold_reasons** | **Dict[str, str]** |  | 

## Example

```python
from winthrop_client_python.models.foia_status_summary_meta import FoiaStatusSummaryMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaStatusSummaryMeta from a JSON string
foia_status_summary_meta_instance = FoiaStatusSummaryMeta.from_json(json)
# print the JSON string representation of the object
print(FoiaStatusSummaryMeta.to_json())

# convert the object into a dict
foia_status_summary_meta_dict = foia_status_summary_meta_instance.to_dict()
# create an instance of FoiaStatusSummaryMeta from a dict
foia_status_summary_meta_from_dict = FoiaStatusSummaryMeta.from_dict(foia_status_summary_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


