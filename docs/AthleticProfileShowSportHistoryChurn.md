# AthleticProfileShowSportHistoryChurn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transitions** | [**List[AthleticProfileShowSportHistoryChurnTransitionsInner]**](AthleticProfileShowSportHistoryChurnTransitionsInner.md) | Seams between adjacent recorded seasons whose head-coach seat changed, oldest first. | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_history_churn import AthleticProfileShowSportHistoryChurn

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportHistoryChurn from a JSON string
athletic_profile_show_sport_history_churn_instance = AthleticProfileShowSportHistoryChurn.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportHistoryChurn.to_json())

# convert the object into a dict
athletic_profile_show_sport_history_churn_dict = athletic_profile_show_sport_history_churn_instance.to_dict()
# create an instance of AthleticProfileShowSportHistoryChurn from a dict
athletic_profile_show_sport_history_churn_from_dict = AthleticProfileShowSportHistoryChurn.from_dict(athletic_profile_show_sport_history_churn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


