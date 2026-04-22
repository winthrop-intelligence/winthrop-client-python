# TeamScheduleSearchResult

Enriched team schedule search result with contacts, RPI, returning percentages, and guarantee data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**last_rpi** | **int** | Most recent RPI ranking | [optional] 
**avg_rpi** | **int** | 5-year average RPI ranking | [optional] 
**distance** | **float** | Distance in miles from user&#39;s school | [optional] 
**avg_guarantee_paid_cents** | **int** |  | [optional] 
**avg_guarantee_received_cents** | **int** |  | [optional] 
**previous_season_record** | **str** | Win-loss record from previous season (e.g. \&quot;22-12\&quot;) | [optional] 
**non_conf_games_current** | **int** | Non-conference games scheduled for current season | [optional] 
**non_conf_games_next** | **int** | Non-conference games scheduled for next season | [optional] 
**school_logo_url** | **str** | URL to school logo image (small variant) | [optional] 
**fil_team_id** | **str** | FilTeam ID as string to avoid precision loss | [optional] 
**returning_pts_pct** | **int** | Percentage of points returning next season | [optional] 
**returning_reb_pct** | **int** | Percentage of rebounds returning next season | [optional] 
**returning_ast_pct** | **int** | Percentage of assists returning next season | [optional] 
**contacts** | [**List[TeamScheduleContact]**](TeamScheduleContact.md) | Scheduling contacts for the school/sport | [optional] 
**home_contracts** | [**TeamScheduleSearchResultHomeContracts**](TeamScheduleSearchResultHomeContracts.md) |  | [optional] 
**away_contracts** | [**TeamScheduleSearchResultAwayContracts**](TeamScheduleSearchResultAwayContracts.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_search_result import TeamScheduleSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleSearchResult from a JSON string
team_schedule_search_result_instance = TeamScheduleSearchResult.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleSearchResult.to_json())

# convert the object into a dict
team_schedule_search_result_dict = team_schedule_search_result_instance.to_dict()
# create an instance of TeamScheduleSearchResult from a dict
team_schedule_search_result_from_dict = TeamScheduleSearchResult.from_dict(team_schedule_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


