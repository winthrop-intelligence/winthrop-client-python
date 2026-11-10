# AdminCompensationSchool

Display school from the first linked position's season, falling back to the stored school for unlinked rows and placeholders. school_id remains the stored editing identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name_or_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_compensation_school import AdminCompensationSchool

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCompensationSchool from a JSON string
admin_compensation_school_instance = AdminCompensationSchool.from_json(json)
# print the JSON string representation of the object
print(AdminCompensationSchool.to_json())

# convert the object into a dict
admin_compensation_school_dict = admin_compensation_school_instance.to_dict()
# create an instance of AdminCompensationSchool from a dict
admin_compensation_school_from_dict = AdminCompensationSchool.from_dict(admin_compensation_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


