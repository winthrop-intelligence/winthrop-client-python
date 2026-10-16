# AdminContactList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminContact]**](AdminContact.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_contact_list import AdminContactList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContactList from a JSON string
admin_contact_list_instance = AdminContactList.from_json(json)
# print the JSON string representation of the object
print(AdminContactList.to_json())

# convert the object into a dict
admin_contact_list_dict = admin_contact_list_instance.to_dict()
# create an instance of AdminContactList from a dict
admin_contact_list_from_dict = AdminContactList.from_dict(admin_contact_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


