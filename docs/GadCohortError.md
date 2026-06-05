# GadCohortError

Structured error returned when a cohort input is unsupported or required filters are missing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**valid_values** | **List[str]** | Supported cohort names when error_type is unsupported_cohort. | [optional] 
**suggested_fix** | **str** |  | [optional] 
**received_args** | **Dict[str, object]** |  | [optional] 
**retryable** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.gad_cohort_error import GadCohortError

# TODO update the JSON string below
json = "{}"
# create an instance of GadCohortError from a JSON string
gad_cohort_error_instance = GadCohortError.from_json(json)
# print the JSON string representation of the object
print(GadCohortError.to_json())

# convert the object into a dict
gad_cohort_error_dict = gad_cohort_error_instance.to_dict()
# create an instance of GadCohortError from a dict
gad_cohort_error_from_dict = GadCohortError.from_dict(gad_cohort_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


