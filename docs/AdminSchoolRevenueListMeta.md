# AdminSchoolRevenueListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**ContactSearchCoachOptionsCoachesInner**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**schools** | [**List[IdName]**](IdName.md) |  | [optional] 
**year_options** | [**List[AdminSchoolRevenueListMetaYearOptionsInner]**](AdminSchoolRevenueListMetaYearOptionsInner.md) |  | [optional] 
**import_failures** | [**List[AdminSchoolRevenueListMetaImportFailuresInner]**](AdminSchoolRevenueListMetaImportFailuresInner.md) | The latest ten failed combined financial imports for this school, newest first. | [optional] 
**jobs** | [**AdminSchoolRevenueListMetaJobs**](AdminSchoolRevenueListMetaJobs.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_revenue_list_meta import AdminSchoolRevenueListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolRevenueListMeta from a JSON string
admin_school_revenue_list_meta_instance = AdminSchoolRevenueListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolRevenueListMeta.to_json())

# convert the object into a dict
admin_school_revenue_list_meta_dict = admin_school_revenue_list_meta_instance.to_dict()
# create an instance of AdminSchoolRevenueListMeta from a dict
admin_school_revenue_list_meta_from_dict = AdminSchoolRevenueListMeta.from_dict(admin_school_revenue_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


