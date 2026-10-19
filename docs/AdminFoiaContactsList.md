# AdminFoiaContactsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminFoiaContact]**](AdminFoiaContact.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_contacts_list import AdminFoiaContactsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaContactsList from a JSON string
admin_foia_contacts_list_instance = AdminFoiaContactsList.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaContactsList.to_json())

# convert the object into a dict
admin_foia_contacts_list_dict = admin_foia_contacts_list_instance.to_dict()
# create an instance of AdminFoiaContactsList from a dict
admin_foia_contacts_list_from_dict = AdminFoiaContactsList.from_dict(admin_foia_contacts_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


