# FoiaInboxContactInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**position** | **str** |  | 
**phone** | **str** |  | 
**mailing_address** | **str** |  | 
**contact_page_url** | **str** |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_contact_input import FoiaInboxContactInput

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxContactInput from a JSON string
foia_inbox_contact_input_instance = FoiaInboxContactInput.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxContactInput.to_json())

# convert the object into a dict
foia_inbox_contact_input_dict = foia_inbox_contact_input_instance.to_dict()
# create an instance of FoiaInboxContactInput from a dict
foia_inbox_contact_input_from_dict = FoiaInboxContactInput.from_dict(foia_inbox_contact_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


