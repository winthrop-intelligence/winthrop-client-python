# FoiaInboxContactEffect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**idempotency_key** | **str** |  | 
**expected_collection_sha256** | **str** |  | 
**contact** | [**FoiaInboxContactInput**](FoiaInboxContactInput.md) |  | 
**contact_id** | **int** |  | 
**expected_contact** | [**FoiaInboxContact**](FoiaInboxContact.md) |  | 
**changes** | [**FoiaInboxContactChanges**](FoiaInboxContactChanges.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_contact_effect import FoiaInboxContactEffect

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxContactEffect from a JSON string
foia_inbox_contact_effect_instance = FoiaInboxContactEffect.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxContactEffect.to_json())

# convert the object into a dict
foia_inbox_contact_effect_dict = foia_inbox_contact_effect_instance.to_dict()
# create an instance of FoiaInboxContactEffect from a dict
foia_inbox_contact_effect_from_dict = FoiaInboxContactEffect.from_dict(foia_inbox_contact_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


