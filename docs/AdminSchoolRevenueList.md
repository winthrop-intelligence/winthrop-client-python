# AdminSchoolRevenueList

A school's financial-uploads console state (admin namespace) — years on file, school picker, year-select options, and Sidekiq import job status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminSchoolRevenueListMeta**](AdminSchoolRevenueListMeta.md) |  | [optional] 
**data** | [**List[AdminSchoolRevenueListDataInner]**](AdminSchoolRevenueListDataInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_revenue_list import AdminSchoolRevenueList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolRevenueList from a JSON string
admin_school_revenue_list_instance = AdminSchoolRevenueList.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolRevenueList.to_json())

# convert the object into a dict
admin_school_revenue_list_dict = admin_school_revenue_list_instance.to_dict()
# create an instance of AdminSchoolRevenueList from a dict
admin_school_revenue_list_from_dict = AdminSchoolRevenueList.from_dict(admin_school_revenue_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


