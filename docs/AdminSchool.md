# AdminSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**school_status** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**allows_foia** | **bool** |  | [optional] 
**cost_of_living_index_city_code** | **str** |  | [optional] 
**primary_conference_name** | **str** |  | [optional] 
**division_name** | **str** |  | [optional] 
**subdivisions** | [**List[AdminCompensationListMetaContractStatusOptionsInner]**](AdminCompensationListMetaContractStatusOptionsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school import AdminSchool

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchool from a JSON string
admin_school_instance = AdminSchool.from_json(json)
# print the JSON string representation of the object
print(AdminSchool.to_json())

# convert the object into a dict
admin_school_dict = admin_school_instance.to_dict()
# create an instance of AdminSchool from a dict
admin_school_from_dict = AdminSchool.from_dict(admin_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


