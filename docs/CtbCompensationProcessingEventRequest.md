# CtbCompensationProcessingEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctb_compensation_processing_event** | [**CtbCompensationProcessingEventInput**](CtbCompensationProcessingEventInput.md) |  | 

## Example

```python
from winthrop_client_python.models.ctb_compensation_processing_event_request import CtbCompensationProcessingEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CtbCompensationProcessingEventRequest from a JSON string
ctb_compensation_processing_event_request_instance = CtbCompensationProcessingEventRequest.from_json(json)
# print the JSON string representation of the object
print(CtbCompensationProcessingEventRequest.to_json())

# convert the object into a dict
ctb_compensation_processing_event_request_dict = ctb_compensation_processing_event_request_instance.to_dict()
# create an instance of CtbCompensationProcessingEventRequest from a dict
ctb_compensation_processing_event_request_from_dict = CtbCompensationProcessingEventRequest.from_dict(ctb_compensation_processing_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


