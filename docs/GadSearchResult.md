# GadSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_contract_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**sport_gender_code_class** | **str** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**home_school_name** | **str** |  | [optional] 
**home_school_short_name** | **str** |  | [optional] 
**home_school_logo_url** | **str** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**away_school_name** | **str** |  | [optional] 
**away_school_short_name** | **str** |  | [optional] 
**away_school_logo_url** | **str** |  | [optional] 
**game_type** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**comp_tbd** | **bool** |  | [optional] 
**variable** | **bool** |  | [optional] 
**cancel_fee_cents** | **int** |  | [optional] 
**cancelled** | **bool** |  | [optional] 
**season_year** | **int** |  | [optional] 
**game_date** | **date** |  | [optional] 
**game_date_tbd** | **bool** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**belongs_to_series** | **bool** |  | [optional] 
**can_manage** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.gad_search_result import GadSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of GadSearchResult from a JSON string
gad_search_result_instance = GadSearchResult.from_json(json)
# print the JSON string representation of the object
print(GadSearchResult.to_json())

# convert the object into a dict
gad_search_result_dict = gad_search_result_instance.to_dict()
# create an instance of GadSearchResult from a dict
gad_search_result_from_dict = GadSearchResult.from_dict(gad_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


