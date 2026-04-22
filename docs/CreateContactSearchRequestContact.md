# CreateContactSearchRequestContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**school_id** | **int** |  | 
**sport_id** | **int** |  | 

## Example

```python
from winthrop_client_python.models.create_contact_search_request_contact import CreateContactSearchRequestContact

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactSearchRequestContact from a JSON string
create_contact_search_request_contact_instance = CreateContactSearchRequestContact.from_json(json)
# print the JSON string representation of the object
print(CreateContactSearchRequestContact.to_json())

# convert the object into a dict
create_contact_search_request_contact_dict = create_contact_search_request_contact_instance.to_dict()
# create an instance of CreateContactSearchRequestContact from a dict
create_contact_search_request_contact_from_dict = CreateContactSearchRequestContact.from_dict(create_contact_search_request_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


