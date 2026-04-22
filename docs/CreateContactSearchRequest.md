# CreateContactSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**CreateContactSearchRequestContact**](CreateContactSearchRequestContact.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_contact_search_request import CreateContactSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactSearchRequest from a JSON string
create_contact_search_request_instance = CreateContactSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateContactSearchRequest.to_json())

# convert the object into a dict
create_contact_search_request_dict = create_contact_search_request_instance.to_dict()
# create an instance of CreateContactSearchRequest from a dict
create_contact_search_request_from_dict = CreateContactSearchRequest.from_dict(create_contact_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


