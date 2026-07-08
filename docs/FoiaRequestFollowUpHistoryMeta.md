# FoiaRequestFollowUpHistoryMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of_date** | **date** |  | [optional] 
**generated_at** | **datetime** |  | [optional] 
**timezone** | **str** |  | [optional] 
**filters_applied** | **Dict[str, object]** |  | [optional] 
**current_page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**max_per_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_request_follow_up_history_meta import FoiaRequestFollowUpHistoryMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaRequestFollowUpHistoryMeta from a JSON string
foia_request_follow_up_history_meta_instance = FoiaRequestFollowUpHistoryMeta.from_json(json)
# print the JSON string representation of the object
print(FoiaRequestFollowUpHistoryMeta.to_json())

# convert the object into a dict
foia_request_follow_up_history_meta_dict = foia_request_follow_up_history_meta_instance.to_dict()
# create an instance of FoiaRequestFollowUpHistoryMeta from a dict
foia_request_follow_up_history_meta_from_dict = FoiaRequestFollowUpHistoryMeta.from_dict(foia_request_follow_up_history_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


