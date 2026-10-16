# AdminContractRequestSearchesOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_season_year** | **int** | Configured current season from SystemSetting | [optional] 
**season_years** | **List[int]** | Descending configured current season plus or minus ten years | [optional] 
**contract_statuses** | [**List[ContactSearchCoachOptionsSportsInner]**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_contract_request_searches_options import AdminContractRequestSearchesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContractRequestSearchesOptions from a JSON string
admin_contract_request_searches_options_instance = AdminContractRequestSearchesOptions.from_json(json)
# print the JSON string representation of the object
print(AdminContractRequestSearchesOptions.to_json())

# convert the object into a dict
admin_contract_request_searches_options_dict = admin_contract_request_searches_options_instance.to_dict()
# create an instance of AdminContractRequestSearchesOptions from a dict
admin_contract_request_searches_options_from_dict = AdminContractRequestSearchesOptions.from_dict(admin_contract_request_searches_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


