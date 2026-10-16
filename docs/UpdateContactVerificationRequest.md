# UpdateContactVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**UpdateContactVerificationRequestContact**](UpdateContactVerificationRequestContact.md) |  | 

## Example

```python
from winthrop_client_python.models.update_contact_verification_request import UpdateContactVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactVerificationRequest from a JSON string
update_contact_verification_request_instance = UpdateContactVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateContactVerificationRequest.to_json())

# convert the object into a dict
update_contact_verification_request_dict = update_contact_verification_request_instance.to_dict()
# create an instance of UpdateContactVerificationRequest from a dict
update_contact_verification_request_from_dict = UpdateContactVerificationRequest.from_dict(update_contact_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


