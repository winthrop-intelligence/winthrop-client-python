# AdminSchoolRevenueListMetaJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ncaa_financial_report_item_importer** | **List[object]** |  | [optional] 
**school_financial_import_job** | **List[object]** |  | [optional] 
**revenue_importer** | **List[object]** |  | [optional] 
**financial_stat_importer** | **List[object]** |  | [optional] 
**financial_infos_importer** | **List[object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_revenue_list_meta_jobs import AdminSchoolRevenueListMetaJobs

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolRevenueListMetaJobs from a JSON string
admin_school_revenue_list_meta_jobs_instance = AdminSchoolRevenueListMetaJobs.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolRevenueListMetaJobs.to_json())

# convert the object into a dict
admin_school_revenue_list_meta_jobs_dict = admin_school_revenue_list_meta_jobs_instance.to_dict()
# create an instance of AdminSchoolRevenueListMetaJobs from a dict
admin_school_revenue_list_meta_jobs_from_dict = AdminSchoolRevenueListMetaJobs.from_dict(admin_school_revenue_list_meta_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


