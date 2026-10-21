# AdminFinancialsQcListMetaAllOfFilterOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conferences** | [**List[IdName]**](IdName.md) |  | [optional] 
**divisions** | [**List[IdName]**](IdName.md) |  | [optional] 
**subdivisions** | [**List[IdName]**](IdName.md) |  | [optional] 
**schools** | [**List[IdName]**](IdName.md) |  | [optional] 
**years** | [**List[AdminFinancialsQcListMetaAllOfFilterOptionsYearsInner]**](AdminFinancialsQcListMetaAllOfFilterOptionsYearsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_financials_qc_list_meta_all_of_filter_options import AdminFinancialsQcListMetaAllOfFilterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFinancialsQcListMetaAllOfFilterOptions from a JSON string
admin_financials_qc_list_meta_all_of_filter_options_instance = AdminFinancialsQcListMetaAllOfFilterOptions.from_json(json)
# print the JSON string representation of the object
print(AdminFinancialsQcListMetaAllOfFilterOptions.to_json())

# convert the object into a dict
admin_financials_qc_list_meta_all_of_filter_options_dict = admin_financials_qc_list_meta_all_of_filter_options_instance.to_dict()
# create an instance of AdminFinancialsQcListMetaAllOfFilterOptions from a dict
admin_financials_qc_list_meta_all_of_filter_options_from_dict = AdminFinancialsQcListMetaAllOfFilterOptions.from_dict(admin_financials_qc_list_meta_all_of_filter_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


