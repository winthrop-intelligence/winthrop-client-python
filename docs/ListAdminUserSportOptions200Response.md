# ListAdminUserSportOptions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedulable** | [**List[IdName]**](IdName.md) |  | 
**permissible** | [**List[IdName]**](IdName.md) |  | 

## Example

```python
from winthrop_client_python.models.list_admin_user_sport_options200_response import ListAdminUserSportOptions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAdminUserSportOptions200Response from a JSON string
list_admin_user_sport_options200_response_instance = ListAdminUserSportOptions200Response.from_json(json)
# print the JSON string representation of the object
print(ListAdminUserSportOptions200Response.to_json())

# convert the object into a dict
list_admin_user_sport_options200_response_dict = list_admin_user_sport_options200_response_instance.to_dict()
# create an instance of ListAdminUserSportOptions200Response from a dict
list_admin_user_sport_options200_response_from_dict = ListAdminUserSportOptions200Response.from_dict(list_admin_user_sport_options200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


