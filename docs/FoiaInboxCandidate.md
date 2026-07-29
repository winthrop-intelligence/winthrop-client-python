# FoiaInboxCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request_id** | **int** |  | 
**foia_request_admin_url** | **str** |  | [optional] 
**school** | [**FoiaInboxSchool**](FoiaInboxSchool.md) |  | 
**foia_label** | [**FoiaInboxLabel**](FoiaInboxLabel.md) |  | 
**state** | **str** |  | 
**status** | **str** |  | 
**date_sent** | **date** |  | [optional] 
**updated_by_school** | **date** |  | [optional] 
**updated_by_wi** | **date** |  | [optional] 
**follow_up_date** | **date** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**foia_notes_sha256** | **str** |  | 
**foia_notes** | [**List[FoiaInboxNote]**](FoiaInboxNote.md) |  | [optional] 
**requested_items** | [**List[FoiaInboxRequestedItem]**](FoiaInboxRequestedItem.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_candidate import FoiaInboxCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxCandidate from a JSON string
foia_inbox_candidate_instance = FoiaInboxCandidate.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxCandidate.to_json())

# convert the object into a dict
foia_inbox_candidate_dict = foia_inbox_candidate_instance.to_dict()
# create an instance of FoiaInboxCandidate from a dict
foia_inbox_candidate_from_dict = FoiaInboxCandidate.from_dict(foia_inbox_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


