# CtbCompensationExpectedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**updated_at** | **datetime** |  | 
**updated_by_school** | **date** |  | 
**updated_by_wi** | **date** |  | 
**foia_notes_sha256** | **str** |  | 

## Example

```python
from winthrop_client_python.models.ctb_compensation_expected_request import CtbCompensationExpectedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CtbCompensationExpectedRequest from a JSON string
ctb_compensation_expected_request_instance = CtbCompensationExpectedRequest.from_json(json)
# print the JSON string representation of the object
print(CtbCompensationExpectedRequest.to_json())

# convert the object into a dict
ctb_compensation_expected_request_dict = ctb_compensation_expected_request_instance.to_dict()
# create an instance of CtbCompensationExpectedRequest from a dict
ctb_compensation_expected_request_from_dict = CtbCompensationExpectedRequest.from_dict(ctb_compensation_expected_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


