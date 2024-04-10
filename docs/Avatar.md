# Avatar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_url** | **str** | Signed, expiring url for the original logo image | [optional] 
**medium_url** | **str** | Signed, expiring url for the medium logo image | [optional] 
**small_url** | **str** | Signed, expiring url for the small logo image | [optional] 
**image_remote_url** | **str** | Remote URL for Coach Avatar | [optional] 

## Example

```python
from winthrop_client_python.models.avatar import Avatar

# TODO update the JSON string below
json = "{}"
# create an instance of Avatar from a JSON string
avatar_instance = Avatar.from_json(json)
# print the JSON string representation of the object
print(Avatar.to_json())

# convert the object into a dict
avatar_dict = avatar_instance.to_dict()
# create an instance of Avatar from a dict
avatar_form_dict = avatar.from_dict(avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


