# FoiaFollowUpReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**FoiaFollowUpReportMeta**](FoiaFollowUpReportMeta.md) |  | [optional] 
**data** | [**List[FoiaFollowUpReportRow]**](FoiaFollowUpReportRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_follow_up_report_response import FoiaFollowUpReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowUpReportResponse from a JSON string
foia_follow_up_report_response_instance = FoiaFollowUpReportResponse.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowUpReportResponse.to_json())

# convert the object into a dict
foia_follow_up_report_response_dict = foia_follow_up_report_response_instance.to_dict()
# create an instance of FoiaFollowUpReportResponse from a dict
foia_follow_up_report_response_from_dict = FoiaFollowUpReportResponse.from_dict(foia_follow_up_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


