# CoachCompensationTabSidebarContractsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**start_on** | **str** |  | [optional] 
**end_on** | **str** |  | [optional] 
**at_will** | **bool** |  | [optional] 
**has_file** | **bool** |  | [optional] 
**can_download** | **bool** |  | [optional] 
**asset_file_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_compensation_tab_sidebar_contracts_inner import CoachCompensationTabSidebarContractsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensationTabSidebarContractsInner from a JSON string
coach_compensation_tab_sidebar_contracts_inner_instance = CoachCompensationTabSidebarContractsInner.from_json(json)
# print the JSON string representation of the object
print(CoachCompensationTabSidebarContractsInner.to_json())

# convert the object into a dict
coach_compensation_tab_sidebar_contracts_inner_dict = coach_compensation_tab_sidebar_contracts_inner_instance.to_dict()
# create an instance of CoachCompensationTabSidebarContractsInner from a dict
coach_compensation_tab_sidebar_contracts_inner_from_dict = CoachCompensationTabSidebarContractsInner.from_dict(coach_compensation_tab_sidebar_contracts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


