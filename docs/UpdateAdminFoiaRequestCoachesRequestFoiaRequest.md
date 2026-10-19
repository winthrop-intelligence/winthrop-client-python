# UpdateAdminFoiaRequestCoachesRequestFoiaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensation_ids** | **List[int]** |  | [optional] 
**compensation_position_ids** | **List[int]** |  | [optional] 
**income_report_ids** | **List[int]** |  | [optional] 
**income_report_position_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_foia_request_coaches_request_foia_request import UpdateAdminFoiaRequestCoachesRequestFoiaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminFoiaRequestCoachesRequestFoiaRequest from a JSON string
update_admin_foia_request_coaches_request_foia_request_instance = UpdateAdminFoiaRequestCoachesRequestFoiaRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminFoiaRequestCoachesRequestFoiaRequest.to_json())

# convert the object into a dict
update_admin_foia_request_coaches_request_foia_request_dict = update_admin_foia_request_coaches_request_foia_request_instance.to_dict()
# create an instance of UpdateAdminFoiaRequestCoachesRequestFoiaRequest from a dict
update_admin_foia_request_coaches_request_foia_request_from_dict = UpdateAdminFoiaRequestCoachesRequestFoiaRequest.from_dict(update_admin_foia_request_coaches_request_foia_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


