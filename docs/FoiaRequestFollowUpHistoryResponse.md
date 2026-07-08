# FoiaRequestFollowUpHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**FoiaRequestFollowUpHistoryMeta**](FoiaRequestFollowUpHistoryMeta.md) |  | [optional] 
**data** | [**List[FoiaRequestFollowUpHistoryRow]**](FoiaRequestFollowUpHistoryRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_request_follow_up_history_response import FoiaRequestFollowUpHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaRequestFollowUpHistoryResponse from a JSON string
foia_request_follow_up_history_response_instance = FoiaRequestFollowUpHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(FoiaRequestFollowUpHistoryResponse.to_json())

# convert the object into a dict
foia_request_follow_up_history_response_dict = foia_request_follow_up_history_response_instance.to_dict()
# create an instance of FoiaRequestFollowUpHistoryResponse from a dict
foia_request_follow_up_history_response_from_dict = FoiaRequestFollowUpHistoryResponse.from_dict(foia_request_follow_up_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


