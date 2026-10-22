# DeskReportSummaryCover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treatment** | **str** |  | 
**kicker** | **str** |  | 
**numeral** | **str** |  | 

## Example

```python
from winthrop_client_python.models.desk_report_summary_cover import DeskReportSummaryCover

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportSummaryCover from a JSON string
desk_report_summary_cover_instance = DeskReportSummaryCover.from_json(json)
# print the JSON string representation of the object
print(DeskReportSummaryCover.to_json())

# convert the object into a dict
desk_report_summary_cover_dict = desk_report_summary_cover_instance.to_dict()
# create an instance of DeskReportSummaryCover from a dict
desk_report_summary_cover_from_dict = DeskReportSummaryCover.from_dict(desk_report_summary_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


