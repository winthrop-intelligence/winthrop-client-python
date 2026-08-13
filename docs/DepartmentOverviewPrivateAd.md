# DepartmentOverviewPrivateAd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**friendly_id** | **str** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**since_year** | **int** |  | 
**years_at_school** | **int** |  | 
**comp** | [**DepartmentOverviewPrivateAdComp**](DepartmentOverviewPrivateAdComp.md) |  | 

## Example

```python
from winthrop_client_python.models.department_overview_private_ad import DepartmentOverviewPrivateAd

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateAd from a JSON string
department_overview_private_ad_instance = DepartmentOverviewPrivateAd.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateAd.to_json())

# convert the object into a dict
department_overview_private_ad_dict = department_overview_private_ad_instance.to_dict()
# create an instance of DepartmentOverviewPrivateAd from a dict
department_overview_private_ad_from_dict = DepartmentOverviewPrivateAd.from_dict(department_overview_private_ad_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


