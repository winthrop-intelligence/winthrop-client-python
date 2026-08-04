# FoiaInboxContactResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotency_key** | **str** |  | 
**action** | **str** |  | 
**status** | **str** |  | 
**contact** | [**FoiaInboxContact**](FoiaInboxContact.md) |  | 
**foia_contacts_sha256** | **str** |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_contact_result import FoiaInboxContactResult

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxContactResult from a JSON string
foia_inbox_contact_result_instance = FoiaInboxContactResult.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxContactResult.to_json())

# convert the object into a dict
foia_inbox_contact_result_dict = foia_inbox_contact_result_instance.to_dict()
# create an instance of FoiaInboxContactResult from a dict
foia_inbox_contact_result_from_dict = FoiaInboxContactResult.from_dict(foia_inbox_contact_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


