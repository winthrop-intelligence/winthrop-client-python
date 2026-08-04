# FoiaInboxReplaceLeadEffect

Updates the current Lead FOIA contact in place; its ID, school, and Lead type are preserved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**idempotency_key** | **str** |  | 
**expected_collection_sha256** | **str** |  | 
**contact_id** | **int** |  | 
**expected_contact** | [**FoiaInboxContact**](FoiaInboxContact.md) |  | 
**contact** | [**FoiaInboxContactInput**](FoiaInboxContactInput.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_replace_lead_effect import FoiaInboxReplaceLeadEffect

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxReplaceLeadEffect from a JSON string
foia_inbox_replace_lead_effect_instance = FoiaInboxReplaceLeadEffect.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxReplaceLeadEffect.to_json())

# convert the object into a dict
foia_inbox_replace_lead_effect_dict = foia_inbox_replace_lead_effect_instance.to_dict()
# create an instance of FoiaInboxReplaceLeadEffect from a dict
foia_inbox_replace_lead_effect_from_dict = FoiaInboxReplaceLeadEffect.from_dict(foia_inbox_replace_lead_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


