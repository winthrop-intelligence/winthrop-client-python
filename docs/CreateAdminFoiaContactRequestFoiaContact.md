# CreateAdminFoiaContactRequestFoiaContact


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
**school_id** | **int** |  | 

## Example

```python
from winthrop_client_python.models.create_admin_foia_contact_request_foia_contact import CreateAdminFoiaContactRequestFoiaContact

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminFoiaContactRequestFoiaContact from a JSON string
create_admin_foia_contact_request_foia_contact_instance = CreateAdminFoiaContactRequestFoiaContact.from_json(json)
# print the JSON string representation of the object
print(CreateAdminFoiaContactRequestFoiaContact.to_json())

# convert the object into a dict
create_admin_foia_contact_request_foia_contact_dict = create_admin_foia_contact_request_foia_contact_instance.to_dict()
# create an instance of CreateAdminFoiaContactRequestFoiaContact from a dict
create_admin_foia_contact_request_foia_contact_from_dict = CreateAdminFoiaContactRequestFoiaContact.from_dict(create_admin_foia_contact_request_foia_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


