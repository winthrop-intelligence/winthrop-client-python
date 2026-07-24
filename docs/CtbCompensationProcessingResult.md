# CtbCompensationProcessingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_series_id** | **str** |  | 
**review_revision_sha256** | **str** |  | 
**decision_sha256** | **str** |  | 
**compensation_exception** | [**CtbCompensationAppliedException**](CtbCompensationAppliedException.md) |  | 

## Example

```python
from winthrop_client_python.models.ctb_compensation_processing_result import CtbCompensationProcessingResult

# TODO update the JSON string below
json = "{}"
# create an instance of CtbCompensationProcessingResult from a JSON string
ctb_compensation_processing_result_instance = CtbCompensationProcessingResult.from_json(json)
# print the JSON string representation of the object
print(CtbCompensationProcessingResult.to_json())

# convert the object into a dict
ctb_compensation_processing_result_dict = ctb_compensation_processing_result_instance.to_dict()
# create an instance of CtbCompensationProcessingResult from a dict
ctb_compensation_processing_result_from_dict = CtbCompensationProcessingResult.from_dict(ctb_compensation_processing_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


