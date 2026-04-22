# UpdateSchoolGroupRequestSchoolGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**school_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_school_group_request_school_group import UpdateSchoolGroupRequestSchoolGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSchoolGroupRequestSchoolGroup from a JSON string
update_school_group_request_school_group_instance = UpdateSchoolGroupRequestSchoolGroup.from_json(json)
# print the JSON string representation of the object
print(UpdateSchoolGroupRequestSchoolGroup.to_json())

# convert the object into a dict
update_school_group_request_school_group_dict = update_school_group_request_school_group_instance.to_dict()
# create an instance of UpdateSchoolGroupRequestSchoolGroup from a dict
update_school_group_request_school_group_from_dict = UpdateSchoolGroupRequestSchoolGroup.from_dict(update_school_group_request_school_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


