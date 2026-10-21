# AdminSubdivisionMembershipsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminCoachContractsQcListMeta**](AdminCoachContractsQcListMeta.md) |  | [optional] 
**data** | [**List[AdminSubdivisionMembership]**](AdminSubdivisionMembership.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_subdivision_memberships_list import AdminSubdivisionMembershipsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSubdivisionMembershipsList from a JSON string
admin_subdivision_memberships_list_instance = AdminSubdivisionMembershipsList.from_json(json)
# print the JSON string representation of the object
print(AdminSubdivisionMembershipsList.to_json())

# convert the object into a dict
admin_subdivision_memberships_list_dict = admin_subdivision_memberships_list_instance.to_dict()
# create an instance of AdminSubdivisionMembershipsList from a dict
admin_subdivision_memberships_list_from_dict = AdminSubdivisionMembershipsList.from_dict(admin_subdivision_memberships_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


