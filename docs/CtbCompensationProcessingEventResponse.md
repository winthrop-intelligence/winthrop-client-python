# CtbCompensationProcessingEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**idempotency_key** | **str** |  | 
**review_series_id** | **str** |  | 
**review_revision_sha256** | **str** |  | 
**decision_sha256** | **str** |  | 
**request_sha256** | **str** |  | 
**foia_request_id** | **int** |  | 
**school_id** | **int** |  | 
**requested_item_id** | **int** |  | 
**compensation_id** | **int** |  | 
**status** | **str** |  | 
**applied_at** | **datetime** |  | 
**result** | [**CtbCompensationProcessingResult**](CtbCompensationProcessingResult.md) |  | 
**idempotent** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.ctb_compensation_processing_event_response import CtbCompensationProcessingEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CtbCompensationProcessingEventResponse from a JSON string
ctb_compensation_processing_event_response_instance = CtbCompensationProcessingEventResponse.from_json(json)
# print the JSON string representation of the object
print(CtbCompensationProcessingEventResponse.to_json())

# convert the object into a dict
ctb_compensation_processing_event_response_dict = ctb_compensation_processing_event_response_instance.to_dict()
# create an instance of CtbCompensationProcessingEventResponse from a dict
ctb_compensation_processing_event_response_from_dict = CtbCompensationProcessingEventResponse.from_dict(ctb_compensation_processing_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


