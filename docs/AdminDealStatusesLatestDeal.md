# AdminDealStatusesLatestDeal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**end_at** | **date** |  | [optional] 
**vendors** | **List[str]** |  | [optional] 
**sports** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deal_statuses_latest_deal import AdminDealStatusesLatestDeal

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDealStatusesLatestDeal from a JSON string
admin_deal_statuses_latest_deal_instance = AdminDealStatusesLatestDeal.from_json(json)
# print the JSON string representation of the object
print(AdminDealStatusesLatestDeal.to_json())

# convert the object into a dict
admin_deal_statuses_latest_deal_dict = admin_deal_statuses_latest_deal_instance.to_dict()
# create an instance of AdminDealStatusesLatestDeal from a dict
admin_deal_statuses_latest_deal_from_dict = AdminDealStatusesLatestDeal.from_dict(admin_deal_statuses_latest_deal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


