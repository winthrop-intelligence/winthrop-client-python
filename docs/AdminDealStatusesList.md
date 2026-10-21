# AdminDealStatusesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminDealStatuses]**](AdminDealStatuses.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deal_statuses_list import AdminDealStatusesList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDealStatusesList from a JSON string
admin_deal_statuses_list_instance = AdminDealStatusesList.from_json(json)
# print the JSON string representation of the object
print(AdminDealStatusesList.to_json())

# convert the object into a dict
admin_deal_statuses_list_dict = admin_deal_statuses_list_instance.to_dict()
# create an instance of AdminDealStatusesList from a dict
admin_deal_statuses_list_from_dict = AdminDealStatusesList.from_dict(admin_deal_statuses_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


