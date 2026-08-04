# FoiaInboxUpdateContactEffect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**idempotency_key** | **str** |  | 
**expected_collection_sha256** | **str** |  | 
**contact_id** | **int** |  | 
**expected_contact** | [**FoiaInboxContact**](FoiaInboxContact.md) |  | 
**changes** | [**FoiaInboxContactChanges**](FoiaInboxContactChanges.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_update_contact_effect import FoiaInboxUpdateContactEffect

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxUpdateContactEffect from a JSON string
foia_inbox_update_contact_effect_instance = FoiaInboxUpdateContactEffect.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxUpdateContactEffect.to_json())

# convert the object into a dict
foia_inbox_update_contact_effect_dict = foia_inbox_update_contact_effect_instance.to_dict()
# create an instance of FoiaInboxUpdateContactEffect from a dict
foia_inbox_update_contact_effect_from_dict = FoiaInboxUpdateContactEffect.from_dict(foia_inbox_update_contact_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


