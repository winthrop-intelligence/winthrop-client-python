# FoiaInboxCandidatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**FoiaInboxCandidatesMeta**](FoiaInboxCandidatesMeta.md) |  | 
**data** | [**List[FoiaInboxCandidate]**](FoiaInboxCandidate.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_candidates_response import FoiaInboxCandidatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxCandidatesResponse from a JSON string
foia_inbox_candidates_response_instance = FoiaInboxCandidatesResponse.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxCandidatesResponse.to_json())

# convert the object into a dict
foia_inbox_candidates_response_dict = foia_inbox_candidates_response_instance.to_dict()
# create an instance of FoiaInboxCandidatesResponse from a dict
foia_inbox_candidates_response_from_dict = FoiaInboxCandidatesResponse.from_dict(foia_inbox_candidates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


