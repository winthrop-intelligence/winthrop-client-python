# AdminContractRequestSearches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_first_name** | **str** |  | [optional] 
**coach_last_name** | **str** |  | [optional] 
**coach_friendly_id** | **str** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**school_short_name** | **str** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**season_year** | **int** |  | [optional] 
**position_title** | **str** |  | [optional] 
**position_type_names** | **List[str]** |  | [optional] 
**compensation_contract_status_id** | **int** |  | [optional] 
**comp_contract_status** | **str** |  | [optional] 
**income_report_contract_status_id** | **int** |  | [optional] 
**oi_contract_status** | **str** |  | [optional] 
**contract_verified** | **bool** |  | [optional] 
**departing** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_contract_request_searches import AdminContractRequestSearches

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContractRequestSearches from a JSON string
admin_contract_request_searches_instance = AdminContractRequestSearches.from_json(json)
# print the JSON string representation of the object
print(AdminContractRequestSearches.to_json())

# convert the object into a dict
admin_contract_request_searches_dict = admin_contract_request_searches_instance.to_dict()
# create an instance of AdminContractRequestSearches from a dict
admin_contract_request_searches_from_dict = AdminContractRequestSearches.from_dict(admin_contract_request_searches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


