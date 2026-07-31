# HumanOverrideResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_post_id** | **int** |  | [optional] 
**outcome** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.human_override_result import HumanOverrideResult

# TODO update the JSON string below
json = "{}"
# create an instance of HumanOverrideResult from a JSON string
human_override_result_instance = HumanOverrideResult.from_json(json)
# print the JSON string representation of the object
print(HumanOverrideResult.to_json())

# convert the object into a dict
human_override_result_dict = human_override_result_instance.to_dict()
# create an instance of HumanOverrideResult from a dict
human_override_result_from_dict = HumanOverrideResult.from_dict(human_override_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


