# ConferenceDepartmentStaffResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**department_name** | **str** |  | [optional] 
**schools** | [**List[DepartmentStaffSchool]**](DepartmentStaffSchool.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.conference_department_staff_response import ConferenceDepartmentStaffResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceDepartmentStaffResponse from a JSON string
conference_department_staff_response_instance = ConferenceDepartmentStaffResponse.from_json(json)
# print the JSON string representation of the object
print(ConferenceDepartmentStaffResponse.to_json())

# convert the object into a dict
conference_department_staff_response_dict = conference_department_staff_response_instance.to_dict()
# create an instance of ConferenceDepartmentStaffResponse from a dict
conference_department_staff_response_from_dict = ConferenceDepartmentStaffResponse.from_dict(conference_department_staff_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


