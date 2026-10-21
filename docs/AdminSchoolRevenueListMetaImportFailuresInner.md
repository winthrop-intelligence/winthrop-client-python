# AdminSchoolRevenueListMetaImportFailuresInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**filenames** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_revenue_list_meta_import_failures_inner import AdminSchoolRevenueListMetaImportFailuresInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolRevenueListMetaImportFailuresInner from a JSON string
admin_school_revenue_list_meta_import_failures_inner_instance = AdminSchoolRevenueListMetaImportFailuresInner.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolRevenueListMetaImportFailuresInner.to_json())

# convert the object into a dict
admin_school_revenue_list_meta_import_failures_inner_dict = admin_school_revenue_list_meta_import_failures_inner_instance.to_dict()
# create an instance of AdminSchoolRevenueListMetaImportFailuresInner from a dict
admin_school_revenue_list_meta_import_failures_inner_from_dict = AdminSchoolRevenueListMetaImportFailuresInner.from_dict(admin_school_revenue_list_meta_import_failures_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


