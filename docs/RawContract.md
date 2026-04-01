# RawContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**asset_file_size** | **int** |  | [optional] 
**asset_content_type** | **str** |  | [optional] 
**asset_file_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**contract_type_id** | **int** |  | [optional] 
**uploaded** | **int** |  | [optional] 
**deal_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_revenue_year** | **int** |  | [optional] 
**audited_financial_year** | **int** |  | [optional] 
**text** | **str** |  | [optional] 
**use_flexpaper** | **bool** |  | [optional] 
**game_contracts_count** | **int** |  | [optional] 
**drive_id** | **str** |  | [optional] 
**migrated_successfully** | **bool** |  | [optional] 
**migration_failure_reason** | **str** |  | [optional] 
**unstract_pdf_text** | **str** |  | [optional] 
**unstract_responses_details** | **str** |  | [optional] 
**layout_preserved_pdf_text** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.raw_contract import RawContract

# TODO update the JSON string below
json = "{}"
# create an instance of RawContract from a JSON string
raw_contract_instance = RawContract.from_json(json)
# print the JSON string representation of the object
print(RawContract.to_json())

# convert the object into a dict
raw_contract_dict = raw_contract_instance.to_dict()
# create an instance of RawContract from a dict
raw_contract_from_dict = RawContract.from_dict(raw_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


