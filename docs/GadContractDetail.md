# GadContractDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**home_school_name** | **str** |  | [optional] 
**home_school_short_name** | **str** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**away_school_name** | **str** |  | [optional] 
**away_school_short_name** | **str** |  | [optional] 
**game_type** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**comp_tbd** | **bool** |  | [optional] 
**variable** | **bool** |  | [optional] 
**cancel_fee_cents** | **int** |  | [optional] 
**cancelled** | **bool** |  | [optional] 
**season_year** | **int** |  | [optional] 
**game_date** | **date** |  | [optional] 
**game_date_tbd** | **str** |  | [optional] 
**signed_on** | **date** |  | [optional] 
**off_site_location** | **str** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**has_raw_contract** | **bool** |  | [optional] 
**raw_contract_url** | **str** |  | [optional] 
**belongs_to_series** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.gad_contract_detail import GadContractDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GadContractDetail from a JSON string
gad_contract_detail_instance = GadContractDetail.from_json(json)
# print the JSON string representation of the object
print(GadContractDetail.to_json())

# convert the object into a dict
gad_contract_detail_dict = gad_contract_detail_instance.to_dict()
# create an instance of GadContractDetail from a dict
gad_contract_detail_from_dict = GadContractDetail.from_dict(gad_contract_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


