# UpdateAdminRankingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference_id** | **int** |  | 
**year** | **str** |  | 
**school** | [**Dict[str, UpdateAdminRankingsRequestSchoolValue]**](UpdateAdminRankingsRequestSchoolValue.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_rankings_request import UpdateAdminRankingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminRankingsRequest from a JSON string
update_admin_rankings_request_instance = UpdateAdminRankingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminRankingsRequest.to_json())

# convert the object into a dict
update_admin_rankings_request_dict = update_admin_rankings_request_instance.to_dict()
# create an instance of UpdateAdminRankingsRequest from a dict
update_admin_rankings_request_from_dict = UpdateAdminRankingsRequest.from_dict(update_admin_rankings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


