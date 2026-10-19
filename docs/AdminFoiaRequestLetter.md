# AdminFoiaRequestLetter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_name** | **str** |  | [optional] 
**request_id** | **int** |  | [optional] 
**portal_site** | **str** |  | [optional] 
**lead_contact** | **str** |  | [optional] 
**cc_emails** | **List[str]** |  | [optional] 
**needs_form** | **bool** |  | [optional] 
**greeting** | **str** |  | [optional] 
**intro** | **str** |  | [optional] 
**closing** | **List[str]** |  | [optional] 
**sections** | [**List[AdminFoiaRequestLetterSectionsInner]**](AdminFoiaRequestLetterSectionsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_letter import AdminFoiaRequestLetter

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestLetter from a JSON string
admin_foia_request_letter_instance = AdminFoiaRequestLetter.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestLetter.to_json())

# convert the object into a dict
admin_foia_request_letter_dict = admin_foia_request_letter_instance.to_dict()
# create an instance of AdminFoiaRequestLetter from a dict
admin_foia_request_letter_from_dict = AdminFoiaRequestLetter.from_dict(admin_foia_request_letter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


