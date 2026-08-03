# HumanOverrideRequestJobPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**human_override_is_athletics** | **bool** |  | 
**expected_source_fingerprint** | **str** | Optional fingerprint of the source snapshot used for the human decision. | [optional] 

## Example

```python
from winthrop_client_python.models.human_override_request_job_post import HumanOverrideRequestJobPost

# TODO update the JSON string below
json = "{}"
# create an instance of HumanOverrideRequestJobPost from a JSON string
human_override_request_job_post_instance = HumanOverrideRequestJobPost.from_json(json)
# print the JSON string representation of the object
print(HumanOverrideRequestJobPost.to_json())

# convert the object into a dict
human_override_request_job_post_dict = human_override_request_job_post_instance.to_dict()
# create an instance of HumanOverrideRequestJobPost from a dict
human_override_request_job_post_from_dict = HumanOverrideRequestJobPost.from_dict(human_override_request_job_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


