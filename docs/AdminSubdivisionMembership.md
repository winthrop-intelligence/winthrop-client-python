# AdminSubdivisionMembership

A school's membership in a subdivision (admin namespace)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**subdivision_id** | **int** |  | [optional] 
**school** | [**ContactSearchCoachOptionsCoachesInner**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**subdivision** | [**ContactSearchCoachOptionsSportsInner**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_subdivision_membership import AdminSubdivisionMembership

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSubdivisionMembership from a JSON string
admin_subdivision_membership_instance = AdminSubdivisionMembership.from_json(json)
# print the JSON string representation of the object
print(AdminSubdivisionMembership.to_json())

# convert the object into a dict
admin_subdivision_membership_dict = admin_subdivision_membership_instance.to_dict()
# create an instance of AdminSubdivisionMembership from a dict
admin_subdivision_membership_from_dict = AdminSubdivisionMembership.from_dict(admin_subdivision_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


