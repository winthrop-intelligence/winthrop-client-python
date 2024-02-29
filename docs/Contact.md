# Contact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print Contact.to_json()

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_form_dict = contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


