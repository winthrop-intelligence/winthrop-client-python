# FoiaStatusSummaryFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overdue_for_update** | **bool** |  | 
**needs_follow_up** | **bool** |  | 
**complete_but_active** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.foia_status_summary_flags import FoiaStatusSummaryFlags

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaStatusSummaryFlags from a JSON string
foia_status_summary_flags_instance = FoiaStatusSummaryFlags.from_json(json)
# print the JSON string representation of the object
print(FoiaStatusSummaryFlags.to_json())

# convert the object into a dict
foia_status_summary_flags_dict = foia_status_summary_flags_instance.to_dict()
# create an instance of FoiaStatusSummaryFlags from a dict
foia_status_summary_flags_from_dict = FoiaStatusSummaryFlags.from_dict(foia_status_summary_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


