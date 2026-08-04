# FoiaInboxContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**type** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**position** | **str** |  | 
**phone** | **str** |  | 
**mailing_address** | **str** |  | 
**contact_page_url** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_contact import FoiaInboxContact

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxContact from a JSON string
foia_inbox_contact_instance = FoiaInboxContact.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxContact.to_json())

# convert the object into a dict
foia_inbox_contact_dict = foia_inbox_contact_instance.to_dict()
# create an instance of FoiaInboxContact from a dict
foia_inbox_contact_from_dict = FoiaInboxContact.from_dict(foia_inbox_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


