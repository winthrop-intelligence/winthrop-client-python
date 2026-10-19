# UpdateAdminFoiaContactRequestFoiaContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**mailing_address** | **str** |  | [optional] 
**contact_page_url** | **str** |  | [optional] 
**school_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_foia_contact_request_foia_contact import UpdateAdminFoiaContactRequestFoiaContact

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminFoiaContactRequestFoiaContact from a JSON string
update_admin_foia_contact_request_foia_contact_instance = UpdateAdminFoiaContactRequestFoiaContact.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminFoiaContactRequestFoiaContact.to_json())

# convert the object into a dict
update_admin_foia_contact_request_foia_contact_dict = update_admin_foia_contact_request_foia_contact_instance.to_dict()
# create an instance of UpdateAdminFoiaContactRequestFoiaContact from a dict
update_admin_foia_contact_request_foia_contact_from_dict = UpdateAdminFoiaContactRequestFoiaContact.from_dict(update_admin_foia_contact_request_foia_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


