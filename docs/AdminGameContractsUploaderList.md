# AdminGameContractsUploaderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminGameContractsUploaderListMeta**](AdminGameContractsUploaderListMeta.md) |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_game_contracts_uploader_list import AdminGameContractsUploaderList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGameContractsUploaderList from a JSON string
admin_game_contracts_uploader_list_instance = AdminGameContractsUploaderList.from_json(json)
# print the JSON string representation of the object
print(AdminGameContractsUploaderList.to_json())

# convert the object into a dict
admin_game_contracts_uploader_list_dict = admin_game_contracts_uploader_list_instance.to_dict()
# create an instance of AdminGameContractsUploaderList from a dict
admin_game_contracts_uploader_list_from_dict = AdminGameContractsUploaderList.from_dict(admin_game_contracts_uploader_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


