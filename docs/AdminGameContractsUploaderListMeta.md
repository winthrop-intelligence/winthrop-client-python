# AdminGameContractsUploaderListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schools** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**sports** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**season_years** | [**List[AdminGameContractsUploaderListMetaSeasonYearsInner]**](AdminGameContractsUploaderListMetaSeasonYearsInner.md) |  | [optional] 
**jobs** | [**List[AdminGameContractUploaderJob]**](AdminGameContractUploaderJob.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_game_contracts_uploader_list_meta import AdminGameContractsUploaderListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGameContractsUploaderListMeta from a JSON string
admin_game_contracts_uploader_list_meta_instance = AdminGameContractsUploaderListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminGameContractsUploaderListMeta.to_json())

# convert the object into a dict
admin_game_contracts_uploader_list_meta_dict = admin_game_contracts_uploader_list_meta_instance.to_dict()
# create an instance of AdminGameContractsUploaderListMeta from a dict
admin_game_contracts_uploader_list_meta_from_dict = AdminGameContractsUploaderListMeta.from_dict(admin_game_contracts_uploader_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


