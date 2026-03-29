# AthleticProfileShowSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**division_name** | **str** |  | [optional] 
**division_id** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**subdivision_name** | **str** |  | [optional] 
**institution_type** | **str** |  | [optional] 
**classification_name** | **str** |  | [optional] 
**usnwr_ranking** | **int** |  | [optional] 
**external_url** | **str** |  | [optional] 
**athletics_url** | **str** |  | [optional] 
**athletics_instagram** | **str** |  | [optional] 
**athletics_twitter** | **str** |  | [optional] 
**institution_instagram** | **str** |  | [optional] 
**institution_twitter** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_school import AthleticProfileShowSchool

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSchool from a JSON string
athletic_profile_show_school_instance = AthleticProfileShowSchool.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSchool.to_json())

# convert the object into a dict
athletic_profile_show_school_dict = athletic_profile_show_school_instance.to_dict()
# create an instance of AthleticProfileShowSchool from a dict
athletic_profile_show_school_from_dict = AthleticProfileShowSchool.from_dict(athletic_profile_show_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


