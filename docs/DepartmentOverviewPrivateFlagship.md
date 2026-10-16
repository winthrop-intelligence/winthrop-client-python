# DepartmentOverviewPrivateFlagship

The programme a private department's Overview banner leads with (WINAD-10391): the highest-paid head-coach seat whose season carries a record, by the DepartmentCoaches seat order. Null when no seat has a W–L.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_key** | **str** |  | 
**sport_name** | **str** |  | 
**coach_name** | **str** |  | 
**season_year** | **int** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**postseason** | **str** |  | 

## Example

```python
from winthrop_client_python.models.department_overview_private_flagship import DepartmentOverviewPrivateFlagship

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateFlagship from a JSON string
department_overview_private_flagship_instance = DepartmentOverviewPrivateFlagship.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateFlagship.to_json())

# convert the object into a dict
department_overview_private_flagship_dict = department_overview_private_flagship_instance.to_dict()
# create an instance of DepartmentOverviewPrivateFlagship from a dict
department_overview_private_flagship_from_dict = DepartmentOverviewPrivateFlagship.from_dict(department_overview_private_flagship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


