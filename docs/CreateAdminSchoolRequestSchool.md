# CreateAdminSchoolRequestSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**anon_name** | **str** |  | [optional] 
**youtube_search_name** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 
**athletics_url** | **str** |  | [optional] 
**wikipedia_url** | **str** |  | [optional] 
**athletics_instagram_handle** | **str** |  | [optional] 
**external_instagram_handle** | **str** |  | [optional] 
**athletics_twitter_handle** | **str** |  | [optional] 
**external_twitter_handle** | **str** |  | [optional] 
**address_1** | **str** |  | [optional] 
**address_2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**cost_of_living_index_city_code** | **str** |  | [optional] 
**school_status** | **str** |  | [optional] 
**athletics_wikipedia_url** | **str** |  | [optional] 
**portal_site** | **str** |  | [optional] 
**portal_password** | **str** |  | [optional] 
**carnegie_id** | **int** |  | [optional] 
**ncaa_id** | **int** |  | [optional] 
**ipeds_unitid** | **int** |  | [optional] 
**state_id** | **int** |  | [optional] 
**primary_conference_id** | **int** |  | [optional] 
**school_classification_id** | **int** |  | [optional] 
**days_to_receive_request** | **int** |  | [optional] 
**private** | **bool** |  | [optional] 
**allows_foia** | **bool** |  | [optional] 
**lawyer_sends** | **bool** |  | [optional] 
**forms** | **bool** |  | [optional] 
**send_oi_reports** | **bool** |  | [optional] 
**mail** | **bool** |  | [optional] 
**subdivision_ids** | **List[int]** |  | [optional] 
**logo_image** | **bytearray** |  | [optional] 
**external_logo_image** | **bytearray** |  | [optional] 
**school_alternate_names_attributes** | [**List[CreateAdminSchoolRequestSchoolSchoolAlternateNamesAttributesInner]**](CreateAdminSchoolRequestSchoolSchoolAlternateNamesAttributesInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_school_request_school import CreateAdminSchoolRequestSchool

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminSchoolRequestSchool from a JSON string
create_admin_school_request_school_instance = CreateAdminSchoolRequestSchool.from_json(json)
# print the JSON string representation of the object
print(CreateAdminSchoolRequestSchool.to_json())

# convert the object into a dict
create_admin_school_request_school_dict = create_admin_school_request_school_instance.to_dict()
# create an instance of CreateAdminSchoolRequestSchool from a dict
create_admin_school_request_school_from_dict = CreateAdminSchoolRequestSchool.from_dict(create_admin_school_request_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


