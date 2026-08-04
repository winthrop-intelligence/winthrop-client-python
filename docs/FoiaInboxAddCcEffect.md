# FoiaInboxAddCcEffect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**idempotency_key** | **str** |  | 
**expected_collection_sha256** | **str** |  | 
**contact** | [**FoiaInboxContactInput**](FoiaInboxContactInput.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_add_cc_effect import FoiaInboxAddCcEffect

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxAddCcEffect from a JSON string
foia_inbox_add_cc_effect_instance = FoiaInboxAddCcEffect.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxAddCcEffect.to_json())

# convert the object into a dict
foia_inbox_add_cc_effect_dict = foia_inbox_add_cc_effect_instance.to_dict()
# create an instance of FoiaInboxAddCcEffect from a dict
foia_inbox_add_cc_effect_from_dict = FoiaInboxAddCcEffect.from_dict(foia_inbox_add_cc_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


