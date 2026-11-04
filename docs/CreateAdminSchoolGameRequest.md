# CreateAdminSchoolGameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game** | [**GameWriteFields**](GameWriteFields.md) |  | 

## Example

```python
from winthrop_client_python.models.create_admin_school_game_request import CreateAdminSchoolGameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminSchoolGameRequest from a JSON string
create_admin_school_game_request_instance = CreateAdminSchoolGameRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminSchoolGameRequest.to_json())

# convert the object into a dict
create_admin_school_game_request_dict = create_admin_school_game_request_instance.to_dict()
# create an instance of CreateAdminSchoolGameRequest from a dict
create_admin_school_game_request_from_dict = CreateAdminSchoolGameRequest.from_dict(create_admin_school_game_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


