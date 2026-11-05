# UpdateAdminRankingsRequestSchoolValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directors_cup_ranking** | **str** |  | [optional] 
**usnwr_ranking** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_rankings_request_school_value import UpdateAdminRankingsRequestSchoolValue

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminRankingsRequestSchoolValue from a JSON string
update_admin_rankings_request_school_value_instance = UpdateAdminRankingsRequestSchoolValue.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminRankingsRequestSchoolValue.to_json())

# convert the object into a dict
update_admin_rankings_request_school_value_dict = update_admin_rankings_request_school_value_instance.to_dict()
# create an instance of UpdateAdminRankingsRequestSchoolValue from a dict
update_admin_rankings_request_school_value_from_dict = UpdateAdminRankingsRequestSchoolValue.from_dict(update_admin_rankings_request_school_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


