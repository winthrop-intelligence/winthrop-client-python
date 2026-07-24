# CtbCompensationProcessingEventInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotency_key** | **str** |  | 
**review_series_id** | **str** |  | 
**review_revision_sha256** | **str** |  | 
**decision_sha256** | **str** |  | 
**foia_request_id** | **int** |  | 
**school_id** | **int** |  | 
**requested_item_id** | **int** |  | 
**compensation_id** | **int** |  | 
**role** | **str** | CTB compensation-availability interpretation selected in the reviewed decision. | 
**actions** | **List[str]** | Granular actions approved for the reviewed not-employed exception. | 
**expected_request** | [**CtbCompensationExpectedRequest**](CtbCompensationExpectedRequest.md) |  | 
**expected_requested_item** | [**FoiaInboxExpectedRequestedItem**](FoiaInboxExpectedRequestedItem.md) |  | 
**expected_compensation** | [**FoiaInboxExpectedCompensation**](FoiaInboxExpectedCompensation.md) |  | 

## Example

```python
from winthrop_client_python.models.ctb_compensation_processing_event_input import CtbCompensationProcessingEventInput

# TODO update the JSON string below
json = "{}"
# create an instance of CtbCompensationProcessingEventInput from a JSON string
ctb_compensation_processing_event_input_instance = CtbCompensationProcessingEventInput.from_json(json)
# print the JSON string representation of the object
print(CtbCompensationProcessingEventInput.to_json())

# convert the object into a dict
ctb_compensation_processing_event_input_dict = ctb_compensation_processing_event_input_instance.to_dict()
# create an instance of CtbCompensationProcessingEventInput from a dict
ctb_compensation_processing_event_input_from_dict = CtbCompensationProcessingEventInput.from_dict(ctb_compensation_processing_event_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


