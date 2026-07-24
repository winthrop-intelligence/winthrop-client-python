# FoiaInboxEffectsFoiaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**updated_by_school** | **date** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_effects_foia_request import FoiaInboxEffectsFoiaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxEffectsFoiaRequest from a JSON string
foia_inbox_effects_foia_request_instance = FoiaInboxEffectsFoiaRequest.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxEffectsFoiaRequest.to_json())

# convert the object into a dict
foia_inbox_effects_foia_request_dict = foia_inbox_effects_foia_request_instance.to_dict()
# create an instance of FoiaInboxEffectsFoiaRequest from a dict
foia_inbox_effects_foia_request_from_dict = FoiaInboxEffectsFoiaRequest.from_dict(foia_inbox_effects_foia_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


