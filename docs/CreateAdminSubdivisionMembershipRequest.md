# CreateAdminSubdivisionMembershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subdivision_membership** | [**CreateAdminSubdivisionMembershipRequestSubdivisionMembership**](CreateAdminSubdivisionMembershipRequestSubdivisionMembership.md) |  | 

## Example

```python
from winthrop_client_python.models.create_admin_subdivision_membership_request import CreateAdminSubdivisionMembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminSubdivisionMembershipRequest from a JSON string
create_admin_subdivision_membership_request_instance = CreateAdminSubdivisionMembershipRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminSubdivisionMembershipRequest.to_json())

# convert the object into a dict
create_admin_subdivision_membership_request_dict = create_admin_subdivision_membership_request_instance.to_dict()
# create an instance of CreateAdminSubdivisionMembershipRequest from a dict
create_admin_subdivision_membership_request_from_dict = CreateAdminSubdivisionMembershipRequest.from_dict(create_admin_subdivision_membership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


