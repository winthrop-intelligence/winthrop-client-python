# FoiaFollowUpGmailSearchHints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_email** | **str** |  | [optional] 
**canonical_domain** | **str** |  | [optional] 
**admin_parity_first_contact_domain** | **str** |  | [optional] 
**lead_email** | **str** |  | [optional] 
**lead_domain** | **str** |  | [optional] 
**after_date** | **date** |  | [optional] 
**suggested_query** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_follow_up_gmail_search_hints import FoiaFollowUpGmailSearchHints

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowUpGmailSearchHints from a JSON string
foia_follow_up_gmail_search_hints_instance = FoiaFollowUpGmailSearchHints.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowUpGmailSearchHints.to_json())

# convert the object into a dict
foia_follow_up_gmail_search_hints_dict = foia_follow_up_gmail_search_hints_instance.to_dict()
# create an instance of FoiaFollowUpGmailSearchHints from a dict
foia_follow_up_gmail_search_hints_from_dict = FoiaFollowUpGmailSearchHints.from_dict(foia_follow_up_gmail_search_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


