# CoachProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**leader** | **bool** |  | 
**hometown_city** | **str** |  | [optional] 
**hometown_state** | **str** |  | [optional] 
**alma_mater_name** | **str** |  | [optional] 
**alma_mater_year** | **int** |  | [optional] 
**twitter_handle** | **str** |  | [optional] 
**twitter_verified** | **bool** |  | 
**linkedin** | **str** |  | [optional] 
**linkedin_verified** | **bool** |  | 
**instagram_handle** | **str** |  | [optional] 
**instagram_verified** | **bool** |  | 
**bio** | **str** |  | [optional] 
**coach_friendly_id** | **str** |  | [optional] 
**departing** | **bool** |  | [optional] 
**current_school_name** | **str** |  | [optional] 
**current_school_id** | **int** |  | [optional] 
**current_sport_name** | **str** |  | [optional] 
**current_position_types** | **List[str]** |  | 
**avatar_url** | **str** |  | [optional] 
**can_see_compensation** | **bool** |  | 
**can_see_videos** | **bool** |  | 
**can_see_coworker_history** | **bool** |  | 
**is_sport_specific** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.coach_profile import CoachProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CoachProfile from a JSON string
coach_profile_instance = CoachProfile.from_json(json)
# print the JSON string representation of the object
print(CoachProfile.to_json())

# convert the object into a dict
coach_profile_dict = coach_profile_instance.to_dict()
# create an instance of CoachProfile from a dict
coach_profile_from_dict = CoachProfile.from_dict(coach_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


