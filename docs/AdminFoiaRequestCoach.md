# AdminFoiaRequestCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**school_name** | **str** |  | [optional] 
**season_year** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**position_id** | **int** |  | [optional] 
**position_type** | **str** |  | [optional] 
**contract** | [**AdminFoiaRequestCoachContract**](AdminFoiaRequestCoachContract.md) |  | [optional] 
**comp_contract_status** | **str** |  | [optional] 
**oi_contract_status** | **str** |  | [optional] 
**compensation_id** | **int** |  | [optional] 
**compensation_attached** | **bool** |  | [optional] 
**compensation_requested_item_id** | **int** |  | [optional] 
**income_report_id** | **int** |  | [optional] 
**income_report_attached** | **bool** |  | [optional] 
**income_report_requested_item_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_coach import AdminFoiaRequestCoach

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestCoach from a JSON string
admin_foia_request_coach_instance = AdminFoiaRequestCoach.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestCoach.to_json())

# convert the object into a dict
admin_foia_request_coach_dict = admin_foia_request_coach_instance.to_dict()
# create an instance of AdminFoiaRequestCoach from a dict
admin_foia_request_coach_from_dict = AdminFoiaRequestCoach.from_dict(admin_foia_request_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


