# GetCompensationComparisons400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | [optional] 
**error_type** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.get_compensation_comparisons400_response import GetCompensationComparisons400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompensationComparisons400Response from a JSON string
get_compensation_comparisons400_response_instance = GetCompensationComparisons400Response.from_json(json)
# print the JSON string representation of the object
print(GetCompensationComparisons400Response.to_json())

# convert the object into a dict
get_compensation_comparisons400_response_dict = get_compensation_comparisons400_response_instance.to_dict()
# create an instance of GetCompensationComparisons400Response from a dict
get_compensation_comparisons400_response_from_dict = GetCompensationComparisons400Response.from_dict(get_compensation_comparisons400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


