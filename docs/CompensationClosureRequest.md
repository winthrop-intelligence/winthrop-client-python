# CompensationClosureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensation_closure** | [**CompensationClosureInput**](CompensationClosureInput.md) |  | 

## Example

```python
from winthrop_client_python.models.compensation_closure_request import CompensationClosureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationClosureRequest from a JSON string
compensation_closure_request_instance = CompensationClosureRequest.from_json(json)
# print the JSON string representation of the object
print(CompensationClosureRequest.to_json())

# convert the object into a dict
compensation_closure_request_dict = compensation_closure_request_instance.to_dict()
# create an instance of CompensationClosureRequest from a dict
compensation_closure_request_from_dict = CompensationClosureRequest.from_dict(compensation_closure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


