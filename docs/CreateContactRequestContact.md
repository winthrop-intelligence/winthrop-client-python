# CreateContactRequestContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**sport_id** | **int** |  | 
**coach_id** | **int** |  | 

## Example

```python
from winthrop_client_python.models.create_contact_request_contact import CreateContactRequestContact

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactRequestContact from a JSON string
create_contact_request_contact_instance = CreateContactRequestContact.from_json(json)
# print the JSON string representation of the object
print(CreateContactRequestContact.to_json())

# convert the object into a dict
create_contact_request_contact_dict = create_contact_request_contact_instance.to_dict()
# create an instance of CreateContactRequestContact from a dict
create_contact_request_contact_from_dict = CreateContactRequestContact.from_dict(create_contact_request_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


