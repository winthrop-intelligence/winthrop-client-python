# CreateCompensationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensation** | [**CompensationCreateRequest**](CompensationCreateRequest.md) |  | 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history (WINAD-10632). Stored on the audit versions this write creates; never returned by the API. Blank is the same as omitted. | [optional] 

## Example

```python
from winthrop_client_python.models.create_compensation_request import CreateCompensationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompensationRequest from a JSON string
create_compensation_request_instance = CreateCompensationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCompensationRequest.to_json())

# convert the object into a dict
create_compensation_request_dict = create_compensation_request_instance.to_dict()
# create an instance of CreateCompensationRequest from a dict
create_compensation_request_from_dict = CreateCompensationRequest.from_dict(create_compensation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


