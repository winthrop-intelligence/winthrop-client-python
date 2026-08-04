# FoiaInboxContactChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**mailing_address** | **str** |  | [optional] 
**contact_page_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_contact_changes import FoiaInboxContactChanges

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxContactChanges from a JSON string
foia_inbox_contact_changes_instance = FoiaInboxContactChanges.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxContactChanges.to_json())

# convert the object into a dict
foia_inbox_contact_changes_dict = foia_inbox_contact_changes_instance.to_dict()
# create an instance of FoiaInboxContactChanges from a dict
foia_inbox_contact_changes_from_dict = FoiaInboxContactChanges.from_dict(foia_inbox_contact_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


