# FoiaFollowUpContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**mailing_address** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**used_for_gmail_hinting** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_follow_up_contact import FoiaFollowUpContact

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowUpContact from a JSON string
foia_follow_up_contact_instance = FoiaFollowUpContact.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowUpContact.to_json())

# convert the object into a dict
foia_follow_up_contact_dict = foia_follow_up_contact_instance.to_dict()
# create an instance of FoiaFollowUpContact from a dict
foia_follow_up_contact_from_dict = FoiaFollowUpContact.from_dict(foia_follow_up_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


