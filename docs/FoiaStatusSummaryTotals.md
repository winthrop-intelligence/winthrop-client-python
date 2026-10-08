# FoiaStatusSummaryTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_label_count** | **int** |  | 
**active_count** | **int** |  | 
**closed_count** | **int** |  | 
**total_count** | **int** |  | 
**active_percentage** | **float** | Active requests divided by all requests, expressed as a percentage from 0 to 100. | 
**overdue_for_update_count** | **int** |  | 
**needs_follow_up_count** | **int** |  | 
**complete_but_active_count** | **int** |  | 

## Example

```python
from winthrop_client_python.models.foia_status_summary_totals import FoiaStatusSummaryTotals

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaStatusSummaryTotals from a JSON string
foia_status_summary_totals_instance = FoiaStatusSummaryTotals.from_json(json)
# print the JSON string representation of the object
print(FoiaStatusSummaryTotals.to_json())

# convert the object into a dict
foia_status_summary_totals_dict = foia_status_summary_totals_instance.to_dict()
# create an instance of FoiaStatusSummaryTotals from a dict
foia_status_summary_totals_from_dict = FoiaStatusSummaryTotals.from_dict(foia_status_summary_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


