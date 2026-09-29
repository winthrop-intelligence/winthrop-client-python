# FoiaInboxEffectsFoiaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**updated_by_school** | **date** |  | [optional] 
**updated_by_wi** | **date** |  | [optional] 
**follow_up_date** | **date** | Exact ISO-8601 follow-up date; omission never clears the date and null is rejected. Mutually exclusive with reset_follow_up_date. Explicit dates survive status, date_sent, and updated_by_wi recalculation until replaced by another explicit date, reset, or the admin \&quot;Mark as Followed Up\&quot; action. Requires expected_request.follow_up_date, follow_up_date_explicit, and updated_at. | [optional] 
**reset_follow_up_date** | **bool** | Clears the explicit marker and immediately recalculates the default follow-up date. Only literal true is accepted; null and false are rejected. Omission never clears the date. Mutually exclusive with follow_up_date. Requires expected_request.follow_up_date, follow_up_date_explicit, and updated_at. | [optional] 
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


