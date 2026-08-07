# AthleticProfileShowSportOverviewHeadCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**last_name** | **str** | Structured last name — may be multi-word (\&quot;Hughley Jr\&quot;). | [optional] 
**interim** | **bool** | True when the resolved seat-holder&#39;s position is interim-only. | [optional] 
**first_season_year** | **int** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**comp_rank** | **int** |  | [optional] 
**comp_cohort_size** | **int** |  | [optional] 
**comp_median_cents** | **int** |  | [optional] 
**contract_start_on** | **date** |  | [optional] 
**contract_end_on** | **date** |  | [optional] 
**contract_on_file** | **bool** |  | [optional] 
**assistant_count** | **int** |  | [optional] 
**staff_pool_cents** | **int** |  | [optional] 
**staff_pool_all_on_file** | **bool** |  | [optional] 
**staff_pool_on_file_count** | **int** | Assistants on the season&#39;s staff whose compensation has a filed contract, so the card can give a partly-filed pool its provenance (\&quot;$825,000 · 4 of 5 on file\&quot;). Null when compensation is not permitted or the season has no staff on file.  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_overview_head_coach import AthleticProfileShowSportOverviewHeadCoach

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportOverviewHeadCoach from a JSON string
athletic_profile_show_sport_overview_head_coach_instance = AthleticProfileShowSportOverviewHeadCoach.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportOverviewHeadCoach.to_json())

# convert the object into a dict
athletic_profile_show_sport_overview_head_coach_dict = athletic_profile_show_sport_overview_head_coach_instance.to_dict()
# create an instance of AthleticProfileShowSportOverviewHeadCoach from a dict
athletic_profile_show_sport_overview_head_coach_from_dict = AthleticProfileShowSportOverviewHeadCoach.from_dict(athletic_profile_show_sport_overview_head_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


