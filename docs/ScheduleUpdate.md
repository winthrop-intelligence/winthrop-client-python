# ScheduleUpdate

One school's most-recent schedule change for the \"Recently Updated\" dashboard module (WINAD-9930). Counts are aggregated over the 24h window ending at updated_at; the row text is assembled client-side.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**school_name** | **str** |  | 
**school_logo_url** | **str** | Logo URL; null when the school has no logo (falls back to initials) | [optional] 
**rank** | **int** | Sport-appropriate ranking (NET for basketball, AP for football, else RPI) | [optional] 
**games_added** | **int** | Games added to the school&#39;s schedule in the window | 
**single_game_date** | **date** | Date of the lone added game; null unless games_added &#x3D;&#x3D; 1 | [optional] 
**dates_added** | **int** | New open availability dates posted in the window | 
**deal_type** | **str** | Representative deal type of the added availabilities; null when none applies | [optional] 
**deal_type_count** | **int** | Count of added dates of that deal type; only set for buy/sell | [optional] 
**updated_at** | **datetime** | The school&#39;s most-recent schedule-update timestamp (sort key) | 
**schedule_profile_eligible** | **bool** | WINAD-10097 - whether the school has a supported D1/D2 schedule profile. When false the frontend renders the school name as plain text instead of linking to /schedules/:sport/:school_id. | 

## Example

```python
from winthrop_client_python.models.schedule_update import ScheduleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleUpdate from a JSON string
schedule_update_instance = ScheduleUpdate.from_json(json)
# print the JSON string representation of the object
print(ScheduleUpdate.to_json())

# convert the object into a dict
schedule_update_dict = schedule_update_instance.to_dict()
# create an instance of ScheduleUpdate from a dict
schedule_update_from_dict = ScheduleUpdate.from_dict(schedule_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


