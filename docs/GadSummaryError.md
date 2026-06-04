# GadSummaryError

Structured error returned when include_school_summary inputs are invalid (missing sport or school).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**valid_values** | **List[str]** | Supported values when error_type is invalid_season_window. | [optional] 
**suggested_fix** | **str** |  | [optional] 
**received_args** | **Dict[str, object]** |  | [optional] 
**retryable** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.gad_summary_error import GadSummaryError

# TODO update the JSON string below
json = "{}"
# create an instance of GadSummaryError from a JSON string
gad_summary_error_instance = GadSummaryError.from_json(json)
# print the JSON string representation of the object
print(GadSummaryError.to_json())

# convert the object into a dict
gad_summary_error_dict = gad_summary_error_instance.to_dict()
# create an instance of GadSummaryError from a dict
gad_summary_error_from_dict = GadSummaryError.from_dict(gad_summary_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


