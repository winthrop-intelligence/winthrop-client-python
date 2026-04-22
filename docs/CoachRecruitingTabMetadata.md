# CoachRecruitingTabMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_name** | **str** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**subdivision_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_recruiting_tab_metadata import CoachRecruitingTabMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CoachRecruitingTabMetadata from a JSON string
coach_recruiting_tab_metadata_instance = CoachRecruitingTabMetadata.from_json(json)
# print the JSON string representation of the object
print(CoachRecruitingTabMetadata.to_json())

# convert the object into a dict
coach_recruiting_tab_metadata_dict = coach_recruiting_tab_metadata_instance.to_dict()
# create an instance of CoachRecruitingTabMetadata from a dict
coach_recruiting_tab_metadata_from_dict = CoachRecruitingTabMetadata.from_dict(coach_recruiting_tab_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


