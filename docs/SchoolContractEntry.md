# SchoolContractEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**home_school_name** | **str** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**away_school_name** | **str** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**game_type** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**comp_tbd** | **bool** |  | [optional] 
**variable** | **bool** |  | [optional] 
**season_year** | **int** |  | [optional] 
**game_date** | **date** |  | [optional] 
**game_date_tbd** | **str** |  | [optional] 
**cancel_fee_cents** | **int** |  | [optional] 
**cancelled** | **bool** |  | [optional] 
**has_raw_contract** | **bool** |  | [optional] 
**belongs_to_series** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_contract_entry import SchoolContractEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolContractEntry from a JSON string
school_contract_entry_instance = SchoolContractEntry.from_json(json)
# print the JSON string representation of the object
print(SchoolContractEntry.to_json())

# convert the object into a dict
school_contract_entry_dict = school_contract_entry_instance.to_dict()
# create an instance of SchoolContractEntry from a dict
school_contract_entry_from_dict = SchoolContractEntry.from_dict(school_contract_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


