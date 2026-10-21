# AdminDealStatuses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_deal** | [**AdminDealStatusesLatestDeal**](AdminDealStatusesLatestDeal.md) |  | [optional] 
**foia_notes** | **List[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**deal_type_id** | **int** |  | [optional] 
**deal_status_type_id** | **int** |  | [optional] 
**deal_source_id** | **int** |  | [optional] 
**school** | [**ContactSearchCoachOptionsCoachesInner**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**deal_type** | [**ContactSearchCoachOptionsSportsInner**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 
**deal_status_type** | [**ContactSearchCoachOptionsSportsInner**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 
**deal_source** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 
**source_note** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**auto_renew** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deal_statuses import AdminDealStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDealStatuses from a JSON string
admin_deal_statuses_instance = AdminDealStatuses.from_json(json)
# print the JSON string representation of the object
print(AdminDealStatuses.to_json())

# convert the object into a dict
admin_deal_statuses_dict = admin_deal_statuses_instance.to_dict()
# create an instance of AdminDealStatuses from a dict
admin_deal_statuses_from_dict = AdminDealStatuses.from_dict(admin_deal_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


