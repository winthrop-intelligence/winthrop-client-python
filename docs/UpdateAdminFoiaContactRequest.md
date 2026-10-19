# UpdateAdminFoiaContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_contact** | [**UpdateAdminFoiaContactRequestFoiaContact**](UpdateAdminFoiaContactRequestFoiaContact.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_foia_contact_request import UpdateAdminFoiaContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminFoiaContactRequest from a JSON string
update_admin_foia_contact_request_instance = UpdateAdminFoiaContactRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminFoiaContactRequest.to_json())

# convert the object into a dict
update_admin_foia_contact_request_dict = update_admin_foia_contact_request_instance.to_dict()
# create an instance of UpdateAdminFoiaContactRequest from a dict
update_admin_foia_contact_request_from_dict = UpdateAdminFoiaContactRequest.from_dict(update_admin_foia_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


