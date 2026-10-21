# AdminDealsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminDeal]**](AdminDeal.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deals_list import AdminDealsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDealsList from a JSON string
admin_deals_list_instance = AdminDealsList.from_json(json)
# print the JSON string representation of the object
print(AdminDealsList.to_json())

# convert the object into a dict
admin_deals_list_dict = admin_deals_list_instance.to_dict()
# create an instance of AdminDealsList from a dict
admin_deals_list_from_dict = AdminDealsList.from_dict(admin_deals_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


