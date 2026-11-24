# CompensationClosureInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Why the compensation is not available. volunteer and graduate_assistant also add their position type. | 
**note** | **str** | Operator note, added to the requested item note and as a sentence of the Compensation comment. Existing text is kept. NUL characters are refused. | 
**expected_status** | **str** | The requested item status the caller saw; a mismatch is refused with 409. | 

## Example

```python
from winthrop_client_python.models.compensation_closure_input import CompensationClosureInput

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationClosureInput from a JSON string
compensation_closure_input_instance = CompensationClosureInput.from_json(json)
# print the JSON string representation of the object
print(CompensationClosureInput.to_json())

# convert the object into a dict
compensation_closure_input_dict = compensation_closure_input_instance.to_dict()
# create an instance of CompensationClosureInput from a dict
compensation_closure_input_from_dict = CompensationClosureInput.from_dict(compensation_closure_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


