# UpdateFoiaRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request** | [**UpdateFoiaRequestRequestFoiaRequest**](UpdateFoiaRequestRequestFoiaRequest.md) |  | 

## Example

```python
from winthrop_client_python.models.update_foia_request_request import UpdateFoiaRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFoiaRequestRequest from a JSON string
update_foia_request_request_instance = UpdateFoiaRequestRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFoiaRequestRequest.to_json())

# convert the object into a dict
update_foia_request_request_dict = update_foia_request_request_instance.to_dict()
# create an instance of UpdateFoiaRequestRequest from a dict
update_foia_request_request_from_dict = UpdateFoiaRequestRequest.from_dict(update_foia_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


