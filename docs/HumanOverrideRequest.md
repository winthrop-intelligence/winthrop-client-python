# HumanOverrideRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_post** | [**HumanOverrideRequestJobPost**](HumanOverrideRequestJobPost.md) |  | 

## Example

```python
from winthrop_client_python.models.human_override_request import HumanOverrideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HumanOverrideRequest from a JSON string
human_override_request_instance = HumanOverrideRequest.from_json(json)
# print the JSON string representation of the object
print(HumanOverrideRequest.to_json())

# convert the object into a dict
human_override_request_dict = human_override_request_instance.to_dict()
# create an instance of HumanOverrideRequest from a dict
human_override_request_from_dict = HumanOverrideRequest.from_dict(human_override_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


