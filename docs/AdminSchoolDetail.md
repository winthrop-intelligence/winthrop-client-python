# AdminSchoolDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_season_year** | **int** |  | [optional] 
**financial_reports** | [**List[AdminSchoolDetailFinancialReportsInner]**](AdminSchoolDetailFinancialReportsInner.md) |  | [optional] 
**vendor_status_options** | [**List[AdminCompensationListMetaContractStatusOptionsInner]**](AdminCompensationListMetaContractStatusOptionsInner.md) |  | [optional] 
**vendor_statuses** | [**List[AdminSchoolDetailVendorStatusesInner]**](AdminSchoolDetailVendorStatusesInner.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**allows_foia** | **bool** |  | [optional] 
**short_name** | **str** |  | [optional] 
**anon_name** | **str** |  | [optional] 
**youtube_search_name** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 
**carnegie_id** | **str** |  | [optional] 
**ipeds_unitid** | **int** |  | [optional] 
**ncaa_id** | **str** |  | [optional] 
**athletics_url** | **str** |  | [optional] 
**wikipedia_url** | **str** |  | [optional] 
**athletics_instagram_handle** | **str** |  | [optional] 
**external_instagram_handle** | **str** |  | [optional] 
**athletics_twitter_handle** | **str** |  | [optional] 
**external_twitter_handle** | **str** |  | [optional] 
**address_1** | **str** |  | [optional] 
**address_2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_id** | **int** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**cost_of_living_index_city_code** | **str** |  | [optional] 
**primary_conference_id** | **int** |  | [optional] 
**school_classification_id** | **int** |  | [optional] 
**school_status** | **str** |  | [optional] 
**athletics_wikipedia_url** | **str** |  | [optional] 
**days_to_receive_request** | **int** |  | [optional] 
**lawyer_sends** | **bool** |  | [optional] 
**forms** | **str** |  | [optional] 
**send_oi_reports** | **bool** |  | [optional] 
**mail** | **str** |  | [optional] 
**portal_site** | **str** |  | [optional] 
**portal_password** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**logo_image_url** | **str** |  | [optional] 
**external_logo_image_url** | **str** |  | [optional] 
**state** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 
**primary_conference** | [**AdminSchoolDetailPrimaryConference**](AdminSchoolDetailPrimaryConference.md) |  | [optional] 
**division** | [**AdminCoachHometownState**](AdminCoachHometownState.md) |  | [optional] 
**school_classification** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 
**subdivisions** | [**List[AdminCompensationListMetaContractStatusOptionsInner]**](AdminCompensationListMetaContractStatusOptionsInner.md) |  | [optional] 
**subdivision_ids** | **List[int]** |  | [optional] 
**school_alternate_names** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**mens** | [**List[AdminSchoolSportRow]**](AdminSchoolSportRow.md) | Sport.mens rows, each annotated with this school&#39;s conference for that sport | [optional] 
**womens** | [**List[AdminSchoolSportRow]**](AdminSchoolSportRow.md) |  | [optional] 
**both_gender** | [**List[AdminSchoolSportRow]**](AdminSchoolSportRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_detail import AdminSchoolDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolDetail from a JSON string
admin_school_detail_instance = AdminSchoolDetail.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolDetail.to_json())

# convert the object into a dict
admin_school_detail_dict = admin_school_detail_instance.to_dict()
# create an instance of AdminSchoolDetail from a dict
admin_school_detail_from_dict = AdminSchoolDetail.from_dict(admin_school_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


