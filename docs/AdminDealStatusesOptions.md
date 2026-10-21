# AdminDealStatusesOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal_status_types** | [**List[ContactSearchCoachOptionsSportsInner]**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 
**deal_sources** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**deal_types** | [**List[ContactSearchCoachOptionsSportsInner]**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deal_statuses_options import AdminDealStatusesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDealStatusesOptions from a JSON string
admin_deal_statuses_options_instance = AdminDealStatusesOptions.from_json(json)
# print the JSON string representation of the object
print(AdminDealStatusesOptions.to_json())

# convert the object into a dict
admin_deal_statuses_options_dict = admin_deal_statuses_options_instance.to_dict()
# create an instance of AdminDealStatusesOptions from a dict
admin_deal_statuses_options_from_dict = AdminDealStatusesOptions.from_dict(admin_deal_statuses_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


