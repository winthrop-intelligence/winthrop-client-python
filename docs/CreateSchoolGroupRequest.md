# CreateSchoolGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_group** | [**CreateSchoolGroupRequestSchoolGroup**](CreateSchoolGroupRequestSchoolGroup.md) |  | 

## Example

```python
from winthrop_client_python.models.create_school_group_request import CreateSchoolGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSchoolGroupRequest from a JSON string
create_school_group_request_instance = CreateSchoolGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSchoolGroupRequest.to_json())

# convert the object into a dict
create_school_group_request_dict = create_school_group_request_instance.to_dict()
# create an instance of CreateSchoolGroupRequest from a dict
create_school_group_request_from_dict = CreateSchoolGroupRequest.from_dict(create_school_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


