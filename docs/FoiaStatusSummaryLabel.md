# FoiaStatusSummaryLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_label_id** | **int** |  | 
**foia_label_name** | **str** |  | 
**active_count** | **int** |  | 
**closed_count** | **int** |  | 
**total_count** | **int** |  | 
**active_percentage** | **float** |  | 
**overdue_for_update_count** | **int** |  | 
**overdue_for_update_request_ids** | **List[int]** |  | 
**needs_follow_up_count** | **int** |  | 
**needs_follow_up_request_ids** | **List[int]** |  | 
**complete_but_active_count** | **int** |  | 
**complete_but_active_request_ids** | **List[int]** |  | 

## Example

```python
from winthrop_client_python.models.foia_status_summary_label import FoiaStatusSummaryLabel

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaStatusSummaryLabel from a JSON string
foia_status_summary_label_instance = FoiaStatusSummaryLabel.from_json(json)
# print the JSON string representation of the object
print(FoiaStatusSummaryLabel.to_json())

# convert the object into a dict
foia_status_summary_label_dict = foia_status_summary_label_instance.to_dict()
# create an instance of FoiaStatusSummaryLabel from a dict
foia_status_summary_label_from_dict = FoiaStatusSummaryLabel.from_dict(foia_status_summary_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


