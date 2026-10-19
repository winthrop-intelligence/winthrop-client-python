# AdminFoiaContact

A school's FOIA (public-records) contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**formatted_phone** | **str** |  | [optional] 
**mailing_address** | **str** |  | [optional] 
**contact_page_url** | **str** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school** | [**IdName**](IdName.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_contact import AdminFoiaContact

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaContact from a JSON string
admin_foia_contact_instance = AdminFoiaContact.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaContact.to_json())

# convert the object into a dict
admin_foia_contact_dict = admin_foia_contact_instance.to_dict()
# create an instance of AdminFoiaContact from a dict
admin_foia_contact_from_dict = AdminFoiaContact.from_dict(admin_foia_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


