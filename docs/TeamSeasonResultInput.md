# TeamSeasonResultInput

Body of PUT /team_season_results, sent flat at the top level of the JSON body. Give season_id, or school_id, sport_id and season_year. Every result field is replaced; one left out is stored as null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**season_year** | **int** | Season end year (2023 &#x3D; the 2022-23 season). APR and GSR rows use the academic year the rate measures (2025 for 2024-25), never \&quot;most recent\&quot;. | [optional] 
**result_name** | **str** | Free text, for example ncaa_stage_reached, ncaa_wins, conf_regular_season_finish, conf_tournament_stage, final_ap_rank, apr_single_year, conference_coach_of_year. Coach awards are results too (value &#x3D; the winner; details: coach name, WinAD coach id when known, awarded_by, shared). | 
**result_value** | **str** | Null while unresolved (the lanes disagree, or only one lane found it). Numbers are stored as text. | [optional] 
**details** | **Dict[str, object]** | For example {\&quot;seed\&quot;: 12, \&quot;bid\&quot;: \&quot;auto\&quot;}; for APR {\&quot;academic_year\&quot;: \&quot;2024-25\&quot;, \&quot;single_year\&quot;: 993, \&quot;multiyear\&quot;: 987, \&quot;released\&quot;: \&quot;2025-05-06\&quot;}; for an unresolved result each lane&#39;s value, URL and quote. | [optional] 
**source_url** | **str** | Best source link (official site preferred). | [optional] 
**quote** | **str** | Verbatim text from source_url supporting the value. | [optional] 
**season_anchor** | **str** | Text on that page tying it to this season. | [optional] 
**verification_method** | **str** |  | 
**change_note** | **str** | Why this change is being made, for the internal audit history. It is stored on the audit version this write creates and is never returned. Blank is the same as omitted; a non-string value is refused with 422 (errors.change_note). | [optional] 

## Example

```python
from winthrop_client_python.models.team_season_result_input import TeamSeasonResultInput

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonResultInput from a JSON string
team_season_result_input_instance = TeamSeasonResultInput.from_json(json)
# print the JSON string representation of the object
print(TeamSeasonResultInput.to_json())

# convert the object into a dict
team_season_result_input_dict = team_season_result_input_instance.to_dict()
# create an instance of TeamSeasonResultInput from a dict
team_season_result_input_from_dict = TeamSeasonResultInput.from_dict(team_season_result_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


