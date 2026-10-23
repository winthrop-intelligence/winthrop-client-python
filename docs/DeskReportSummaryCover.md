# DeskReportSummaryCover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treatment** | **str** |  | 
**kicker** | **str** |  | 
**numeral** | **str** |  | 
**image_url** | **str** | Optional cover art for the library card (WINAD-10725). An expiring Active Storage link served under the report&#39;s audience rules: fetch it with the reader&#39;s bearer token, the same way as a download.  | 
**banner_image_url** | **str** | Optional art-only reader header image. When null, the reader header uses image_url. | 

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


