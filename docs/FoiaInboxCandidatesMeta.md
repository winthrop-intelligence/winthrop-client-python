# FoiaInboxCandidatesMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generated_at** | **datetime** |  | 
**filters_applied** | **Dict[str, object]** |  | [optional] 
**current_page** | **int** |  | 
**per_page** | **int** |  | 
**max_per_page** | **int** |  | 
**total_pages** | **int** |  | 
**total_entries** | **int** |  | 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_candidates_meta import FoiaInboxCandidatesMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxCandidatesMeta from a JSON string
foia_inbox_candidates_meta_instance = FoiaInboxCandidatesMeta.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxCandidatesMeta.to_json())

# convert the object into a dict
foia_inbox_candidates_meta_dict = foia_inbox_candidates_meta_instance.to_dict()
# create an instance of FoiaInboxCandidatesMeta from a dict
foia_inbox_candidates_meta_from_dict = FoiaInboxCandidatesMeta.from_dict(foia_inbox_candidates_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


