# CreateAdminCoachRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach** | [**CreateAdminCoachRequestCoach**](CreateAdminCoachRequestCoach.md) |  | 

## Example

```python
from winthrop_client_python.models.create_admin_coach_request import CreateAdminCoachRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminCoachRequest from a JSON string
create_admin_coach_request_instance = CreateAdminCoachRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminCoachRequest.to_json())

# convert the object into a dict
create_admin_coach_request_dict = create_admin_coach_request_instance.to_dict()
# create an instance of CreateAdminCoachRequest from a dict
create_admin_coach_request_from_dict = CreateAdminCoachRequest.from_dict(create_admin_coach_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


