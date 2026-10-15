# CreateAdminCoachProfileMatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**potential_matches** | [**List[AdminCoach]**](AdminCoach.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_coach_profile_match200_response import CreateAdminCoachProfileMatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminCoachProfileMatch200Response from a JSON string
create_admin_coach_profile_match200_response_instance = CreateAdminCoachProfileMatch200Response.from_json(json)
# print the JSON string representation of the object
print(CreateAdminCoachProfileMatch200Response.to_json())

# convert the object into a dict
create_admin_coach_profile_match200_response_dict = create_admin_coach_profile_match200_response_instance.to_dict()
# create an instance of CreateAdminCoachProfileMatch200Response from a dict
create_admin_coach_profile_match200_response_from_dict = CreateAdminCoachProfileMatch200Response.from_dict(create_admin_coach_profile_match200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


