# AthleticProfileShowSportHistory

History tab payload for a sport scope (WINAD-10210); null for ADMIN scope. A decade of seasons with the head-coach seat per year and filed spend where present. Transitions never carry a dollar amount — WinAD stores termination agreements as documents only. Missing values are null, never zero.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**results_lens** | **str** | The results metric this surface is read through, resolved per season from the sport&#39;s rank chain (NET for basketball, CONF_WINS for football, RPI otherwise) with CONF_WINS as the fallback when no rank is filed (WINAD-10259, WINAD-10268). Metric fields ship for every column; the lens names the one a surface may claim. | [optional] 
**seasons** | [**List[AthleticProfileShowSportHistorySeasonsInner]**](AthleticProfileShowSportHistorySeasonsInner.md) | Up to ten season-years ending at season_year, newest first; only recorded seasons appear. | [optional] 
**churn** | [**AthleticProfileShowSportHistoryChurn**](AthleticProfileShowSportHistoryChurn.md) |  | [optional] 
**as_of** | **date** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_history import AthleticProfileShowSportHistory

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportHistory from a JSON string
athletic_profile_show_sport_history_instance = AthleticProfileShowSportHistory.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportHistory.to_json())

# convert the object into a dict
athletic_profile_show_sport_history_dict = athletic_profile_show_sport_history_instance.to_dict()
# create an instance of AthleticProfileShowSportHistory from a dict
athletic_profile_show_sport_history_from_dict = AthleticProfileShowSportHistory.from_dict(athletic_profile_show_sport_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


