# AdminDealsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal_types** | [**List[AdminDealsOptionsDealTypesInner]**](AdminDealsOptionsDealTypesInner.md) |  | [optional] 
**vendors** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**sports** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deals_options import AdminDealsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDealsOptions from a JSON string
admin_deals_options_instance = AdminDealsOptions.from_json(json)
# print the JSON string representation of the object
print(AdminDealsOptions.to_json())

# convert the object into a dict
admin_deals_options_dict = admin_deals_options_instance.to_dict()
# create an instance of AdminDealsOptions from a dict
admin_deals_options_from_dict = AdminDealsOptions.from_dict(admin_deals_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


