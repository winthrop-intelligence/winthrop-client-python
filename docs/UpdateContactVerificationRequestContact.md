# UpdateContactVerificationRequestContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified_scheduling_contact** | **bool** |  | 
**verified_at** | **date** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_contact_verification_request_contact import UpdateContactVerificationRequestContact

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactVerificationRequestContact from a JSON string
update_contact_verification_request_contact_instance = UpdateContactVerificationRequestContact.from_json(json)
# print the JSON string representation of the object
print(UpdateContactVerificationRequestContact.to_json())

# convert the object into a dict
update_contact_verification_request_contact_dict = update_contact_verification_request_contact_instance.to_dict()
# create an instance of UpdateContactVerificationRequestContact from a dict
update_contact_verification_request_contact_from_dict = UpdateContactVerificationRequestContact.from_dict(update_contact_verification_request_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


