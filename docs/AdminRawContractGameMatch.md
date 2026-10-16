# AdminRawContractGameMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**asset_file_name** | **str** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**home_school_name** | **str** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**away_school_name** | **str** |  | [optional] 
**years** | **List[int]** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_raw_contract_game_match import AdminRawContractGameMatch

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRawContractGameMatch from a JSON string
admin_raw_contract_game_match_instance = AdminRawContractGameMatch.from_json(json)
# print the JSON string representation of the object
print(AdminRawContractGameMatch.to_json())

# convert the object into a dict
admin_raw_contract_game_match_dict = admin_raw_contract_game_match_instance.to_dict()
# create an instance of AdminRawContractGameMatch from a dict
admin_raw_contract_game_match_from_dict = AdminRawContractGameMatch.from_dict(admin_raw_contract_game_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


