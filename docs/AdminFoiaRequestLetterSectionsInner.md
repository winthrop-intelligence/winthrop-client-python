# AdminFoiaRequestLetterSectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**heading** | **str** |  | [optional] 
**paragraphs** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_letter_sections_inner import AdminFoiaRequestLetterSectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestLetterSectionsInner from a JSON string
admin_foia_request_letter_sections_inner_instance = AdminFoiaRequestLetterSectionsInner.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestLetterSectionsInner.to_json())

# convert the object into a dict
admin_foia_request_letter_sections_inner_dict = admin_foia_request_letter_sections_inner_instance.to_dict()
# create an instance of AdminFoiaRequestLetterSectionsInner from a dict
admin_foia_request_letter_sections_inner_from_dict = AdminFoiaRequestLetterSectionsInner.from_dict(admin_foia_request_letter_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


