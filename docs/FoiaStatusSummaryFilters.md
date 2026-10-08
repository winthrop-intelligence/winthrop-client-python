# FoiaStatusSummaryFilters

Applied filters; active_labels_only is always true, excluding archived labels.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_label_id** | **int** |  | 
**active_labels_only** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.foia_status_summary_filters import FoiaStatusSummaryFilters

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaStatusSummaryFilters from a JSON string
foia_status_summary_filters_instance = FoiaStatusSummaryFilters.from_json(json)
# print the JSON string representation of the object
print(FoiaStatusSummaryFilters.to_json())

# convert the object into a dict
foia_status_summary_filters_dict = foia_status_summary_filters_instance.to_dict()
# create an instance of FoiaStatusSummaryFilters from a dict
foia_status_summary_filters_from_dict = FoiaStatusSummaryFilters.from_dict(foia_status_summary_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


