# ListAdminGameContracts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminGameContract]**](AdminGameContract.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.list_admin_game_contracts200_response import ListAdminGameContracts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAdminGameContracts200Response from a JSON string
list_admin_game_contracts200_response_instance = ListAdminGameContracts200Response.from_json(json)
# print the JSON string representation of the object
print(ListAdminGameContracts200Response.to_json())

# convert the object into a dict
list_admin_game_contracts200_response_dict = list_admin_game_contracts200_response_instance.to_dict()
# create an instance of ListAdminGameContracts200Response from a dict
list_admin_game_contracts200_response_from_dict = ListAdminGameContracts200Response.from_dict(list_admin_game_contracts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


