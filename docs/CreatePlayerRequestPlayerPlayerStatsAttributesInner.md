# CreatePlayerRequestPlayerPlayerStatsAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**eligibility_year** | **int** |  | [optional] 
**position** | **str** |  | [optional] 
**eligible** | **str** |  | [optional] 
**recruit_year** | **bool** |  | [optional] 
**transfer_year** | **bool** |  | [optional] 
**last_season** | **bool** |  | [optional] 
**player_number** | **int** |  | [optional] 
**average_stars** | **float** |  | [optional] 
**overall_ranking** | **int** |  | [optional] 
**position_ranking** | **int** |  | [optional] 
**points** | **int** |  | [optional] 
**rebounds** | **int** |  | [optional] 
**assists** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_player_request_player_player_stats_attributes_inner import CreatePlayerRequestPlayerPlayerStatsAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlayerRequestPlayerPlayerStatsAttributesInner from a JSON string
create_player_request_player_player_stats_attributes_inner_instance = CreatePlayerRequestPlayerPlayerStatsAttributesInner.from_json(json)
# print the JSON string representation of the object
print(CreatePlayerRequestPlayerPlayerStatsAttributesInner.to_json())

# convert the object into a dict
create_player_request_player_player_stats_attributes_inner_dict = create_player_request_player_player_stats_attributes_inner_instance.to_dict()
# create an instance of CreatePlayerRequestPlayerPlayerStatsAttributesInner from a dict
create_player_request_player_player_stats_attributes_inner_from_dict = CreatePlayerRequestPlayerPlayerStatsAttributesInner.from_dict(create_player_request_player_player_stats_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


