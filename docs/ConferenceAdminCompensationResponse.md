# ConferenceAdminCompensationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**departments** | [**List[IdName]**](IdName.md) |  | [optional] 
**leader_ad_positions** | [**List[IdName]**](IdName.md) |  | [optional] 
**compensations** | [**List[CompensationRow]**](CompensationRow.md) |  | [optional] 
**schools_no_comp** | [**List[SchoolNoComp]**](SchoolNoComp.md) |  | [optional] 
**schools_no_season** | [**List[SchoolNoSeason]**](SchoolNoSeason.md) |  | [optional] 
**subdivisions** | [**List[AdminCompensationSubdivision]**](AdminCompensationSubdivision.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.conference_admin_compensation_response import ConferenceAdminCompensationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceAdminCompensationResponse from a JSON string
conference_admin_compensation_response_instance = ConferenceAdminCompensationResponse.from_json(json)
# print the JSON string representation of the object
print(ConferenceAdminCompensationResponse.to_json())

# convert the object into a dict
conference_admin_compensation_response_dict = conference_admin_compensation_response_instance.to_dict()
# create an instance of ConferenceAdminCompensationResponse from a dict
conference_admin_compensation_response_from_dict = ConferenceAdminCompensationResponse.from_dict(conference_admin_compensation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


