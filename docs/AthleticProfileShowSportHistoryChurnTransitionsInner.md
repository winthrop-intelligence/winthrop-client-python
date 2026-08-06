# AthleticProfileShowSportHistoryChurnTransitionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year** | **int** |  | [optional] 
**from_coach_name** | **str** |  | [optional] 
**to_coach_name** | **str** |  | [optional] 
**settlement_raw_contract_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_history_churn_transitions_inner import AthleticProfileShowSportHistoryChurnTransitionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportHistoryChurnTransitionsInner from a JSON string
athletic_profile_show_sport_history_churn_transitions_inner_instance = AthleticProfileShowSportHistoryChurnTransitionsInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportHistoryChurnTransitionsInner.to_json())

# convert the object into a dict
athletic_profile_show_sport_history_churn_transitions_inner_dict = athletic_profile_show_sport_history_churn_transitions_inner_instance.to_dict()
# create an instance of AthleticProfileShowSportHistoryChurnTransitionsInner from a dict
athletic_profile_show_sport_history_churn_transitions_inner_from_dict = AthleticProfileShowSportHistoryChurnTransitionsInner.from_dict(athletic_profile_show_sport_history_churn_transitions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


