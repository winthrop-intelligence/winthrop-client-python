# UserRequestCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserRequest]**](UserRequest.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.user_request_collection import UserRequestCollection

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequestCollection from a JSON string
user_request_collection_instance = UserRequestCollection.from_json(json)
# print the JSON string representation of the object
print(UserRequestCollection.to_json())

# convert the object into a dict
user_request_collection_dict = user_request_collection_instance.to_dict()
# create an instance of UserRequestCollection from a dict
user_request_collection_from_dict = UserRequestCollection.from_dict(user_request_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


