# AthleticProfileShowSportHistorySeasonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**coach_last_name** | **str** | Structured last name of the seat-holder — may be multi-word (\&quot;Hughley Jr\&quot;), never derived by splitting the full name. | [optional] 
**interim** | **bool** |  | [optional] 
**record** | **str** |  | [optional] 
**conference_record** | **str** |  | [optional] 
**net_rank** | **int** |  | [optional] 
**rpi** | **int** |  | [optional] 
**postseason** | **str** |  | [optional] 
**spend_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_history_seasons_inner import AthleticProfileShowSportHistorySeasonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportHistorySeasonsInner from a JSON string
athletic_profile_show_sport_history_seasons_inner_instance = AthleticProfileShowSportHistorySeasonsInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportHistorySeasonsInner.to_json())

# convert the object into a dict
athletic_profile_show_sport_history_seasons_inner_dict = athletic_profile_show_sport_history_seasons_inner_instance.to_dict()
# create an instance of AthleticProfileShowSportHistorySeasonsInner from a dict
athletic_profile_show_sport_history_seasons_inner_from_dict = AthleticProfileShowSportHistorySeasonsInner.from_dict(athletic_profile_show_sport_history_seasons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


