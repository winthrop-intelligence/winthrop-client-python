# FoiaInboxEffects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request** | [**FoiaInboxEffectsFoiaRequest**](FoiaInboxEffectsFoiaRequest.md) |  | [optional] 
**requested_items** | [**List[FoiaInboxEffectsRequestedItemsInner]**](FoiaInboxEffectsRequestedItemsInner.md) |  | [optional] 
**compensation_exceptions** | [**List[FoiaInboxCompensationException]**](FoiaInboxCompensationException.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_effects import FoiaInboxEffects

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxEffects from a JSON string
foia_inbox_effects_instance = FoiaInboxEffects.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxEffects.to_json())

# convert the object into a dict
foia_inbox_effects_dict = foia_inbox_effects_instance.to_dict()
# create an instance of FoiaInboxEffects from a dict
foia_inbox_effects_from_dict = FoiaInboxEffects.from_dict(foia_inbox_effects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


