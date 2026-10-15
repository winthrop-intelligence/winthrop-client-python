# CreateAdminCoachRequestCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible** | **bool** | Whether the coach is visible to customers. | [optional] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**alternate_name** | **str** |  | [optional] 
**dob** | **date** |  | [optional] 
**gender** | **str** |  | [optional] 
**hometown_city** | **str** |  | [optional] 
**hometown_state_id** | **int** |  | [optional] 
**alma_mater_id** | **int** |  | [optional] 
**alma_mater_year** | **str** |  | [optional] 
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
**avatar_attributes** | [**CreateAdminCoachRequestCoachAvatarAttributes**](CreateAdminCoachRequestCoachAvatarAttributes.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_coach_request_coach import CreateAdminCoachRequestCoach

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminCoachRequestCoach from a JSON string
create_admin_coach_request_coach_instance = CreateAdminCoachRequestCoach.from_json(json)
# print the JSON string representation of the object
print(CreateAdminCoachRequestCoach.to_json())

# convert the object into a dict
create_admin_coach_request_coach_dict = create_admin_coach_request_coach_instance.to_dict()
# create an instance of CreateAdminCoachRequestCoach from a dict
create_admin_coach_request_coach_from_dict = CreateAdminCoachRequestCoach.from_dict(create_admin_coach_request_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


