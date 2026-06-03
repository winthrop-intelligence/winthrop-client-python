# RawContractBackTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator for the back-link target: &#39;coach&#39; for a coach contract, &#39;game&#39; for a game contract. | [optional] 
**id** | **int** | Coach id when type is &#39;coach&#39;. Unused for &#39;game&#39; (use home_school_id / away_school_id instead). | [optional] 
**name** | **str** | Coach name when type is &#39;coach&#39;. Unused for &#39;game&#39;. | [optional] 
**position_title** | **str** | Representative position title for the coach contract (matches the coach profile sidebar contract row). | [optional] 
**position_group** | **str** | Representative position group for the coach contract. | [optional] 
**sport** | **str** | Sport for the coach (representative position) or game contract. | [optional] 
**contract_start_on** | **date** | Coach contract start date. | [optional] 
**contract_end_on** | **date** | Coach contract end date. | [optional] 
**home_school_id** | **int** | Home school id when type is &#39;game&#39;. | [optional] 
**home_school_name** | **str** | Home school name when type is &#39;game&#39;. | [optional] 
**away_school_id** | **int** | Away school id when type is &#39;game&#39;. | [optional] 
**away_school_name** | **str** | Away school name when type is &#39;game&#39;. | [optional] 
**season_year** | **int** | Season year for the game contract (falls back to game_date year). | [optional] 

## Example

```python
from winthrop_client_python.models.raw_contract_back_to import RawContractBackTo

# TODO update the JSON string below
json = "{}"
# create an instance of RawContractBackTo from a JSON string
raw_contract_back_to_instance = RawContractBackTo.from_json(json)
# print the JSON string representation of the object
print(RawContractBackTo.to_json())

# convert the object into a dict
raw_contract_back_to_dict = raw_contract_back_to_instance.to_dict()
# create an instance of RawContractBackTo from a dict
raw_contract_back_to_from_dict = RawContractBackTo.from_dict(raw_contract_back_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


