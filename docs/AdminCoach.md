# AdminCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible** | **bool** |  | [optional] 
**id** | **int** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**alternate_name** | **str** |  | [optional] 
**dob** | **date** |  | [optional] 
**gender** | **str** |  | [optional] 
**hometown_city** | **str** |  | [optional] 
**alma_mater_year** | **str** |  | [optional] 
**years_of_experience** | **int** |  | [optional] 
**external_years_experience** | **int** |  | [optional] 
**diversity** | **bool** |  | [optional] 
**bio** | **str** |  | [optional] 
**bio_text** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_scraping_disabled** | **bool** |  | [optional] 
**phone** | **str** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**twitter_handle** | **str** |  | [optional] 
**twitter_scraping_disabled** | **bool** |  | [optional] 
**facebook** | **str** |  | [optional] 
**linkedin** | **str** |  | [optional] 
**linkedin_scraping_disabled** | **bool** |  | [optional] 
**youtube_search** | **str** |  | [optional] 
**instagram_handle** | **str** |  | [optional] 
**instagram_scraping_disabled** | **bool** |  | [optional] 
**avatar_scraping_disabled** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**hometown_state** | [**AdminCoachHometownState**](AdminCoachHometownState.md) |  | [optional] 
**alma_mater** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 
**avatar** | [**AdminCoachAvatar**](AdminCoachAvatar.md) |  | [optional] 
**current_school** | [**AdminCoachCurrentSchool**](AdminCoachCurrentSchool.md) |  | [optional] 
**current_sport** | [**AdminCoachCurrentSport**](AdminCoachCurrentSport.md) |  | [optional] 
**current_position** | [**AdminCoachCurrentPosition**](AdminCoachCurrentPosition.md) |  | [optional] 
**positions_by_sport** | [**List[AdminCoachPositionsBySportInner]**](AdminCoachPositionsBySportInner.md) |  | [optional] 
**blocked_sections** | [**AdminCoachBlockedSections**](AdminCoachBlockedSections.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach import AdminCoach

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoach from a JSON string
admin_coach_instance = AdminCoach.from_json(json)
# print the JSON string representation of the object
print(AdminCoach.to_json())

# convert the object into a dict
admin_coach_dict = admin_coach_instance.to_dict()
# create an instance of AdminCoach from a dict
admin_coach_from_dict = AdminCoach.from_dict(admin_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


