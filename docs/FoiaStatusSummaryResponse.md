# FoiaStatusSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**FoiaStatusSummaryMeta**](FoiaStatusSummaryMeta.md) |  | 
**totals** | [**FoiaStatusSummaryTotals**](FoiaStatusSummaryTotals.md) |  | 
**labels** | [**List[FoiaStatusSummaryLabel]**](FoiaStatusSummaryLabel.md) |  | 
**data** | [**List[FoiaStatusSummaryRequest]**](FoiaStatusSummaryRequest.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_status_summary_response import FoiaStatusSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaStatusSummaryResponse from a JSON string
foia_status_summary_response_instance = FoiaStatusSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(FoiaStatusSummaryResponse.to_json())

# convert the object into a dict
foia_status_summary_response_dict = foia_status_summary_response_instance.to_dict()
# create an instance of FoiaStatusSummaryResponse from a dict
foia_status_summary_response_from_dict = FoiaStatusSummaryResponse.from_dict(foia_status_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


