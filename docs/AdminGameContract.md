# AdminGameContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**game_date** | **date** |  | [optional] 
**game_date_tbd** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**comp_tbd** | **bool** |  | [optional] 
**variable** | **bool** |  | [optional] 
**cancel_fee_cents** | **int** |  | [optional] 
**cancelled** | **bool** |  | [optional] 
**signed_on** | **date** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**season_year** | **int** |  | [optional] 
**season_year_tbd** | **int** |  | [optional] 
**game_type** | **str** |  | [optional] 
**off_site_location** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**home_school_name** | **str** |  | [optional] 
**away_school_name** | **str** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**belongs_to_series** | **bool** |  | [optional] 
**display_year** | **str** | The Year the old admin pages showed — a linked game&#39;s season year, else the game date&#39;s year, else the TBD date text. | [optional] 
**attendance** | **int** |  | [optional] 
**has_raw_contract** | **bool** |  | [optional] 
**raw_contract_filename** | **str** |  | [optional] 
**raw_contract_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_game_contract import AdminGameContract

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGameContract from a JSON string
admin_game_contract_instance = AdminGameContract.from_json(json)
# print the JSON string representation of the object
print(AdminGameContract.to_json())

# convert the object into a dict
admin_game_contract_dict = admin_game_contract_instance.to_dict()
# create an instance of AdminGameContract from a dict
admin_game_contract_from_dict = AdminGameContract.from_dict(admin_game_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


