# CreateSchoolGroupRequestSchoolGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**school_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_school_group_request_school_group import CreateSchoolGroupRequestSchoolGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSchoolGroupRequestSchoolGroup from a JSON string
create_school_group_request_school_group_instance = CreateSchoolGroupRequestSchoolGroup.from_json(json)
# print the JSON string representation of the object
print(CreateSchoolGroupRequestSchoolGroup.to_json())

# convert the object into a dict
create_school_group_request_school_group_dict = create_school_group_request_school_group_instance.to_dict()
# create an instance of CreateSchoolGroupRequestSchoolGroup from a dict
create_school_group_request_school_group_from_dict = CreateSchoolGroupRequestSchoolGroup.from_dict(create_school_group_request_school_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


