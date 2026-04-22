# UpdateSchoolGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_group** | [**UpdateSchoolGroupRequestSchoolGroup**](UpdateSchoolGroupRequestSchoolGroup.md) |  | 

## Example

```python
from winthrop_client_python.models.update_school_group_request import UpdateSchoolGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSchoolGroupRequest from a JSON string
update_school_group_request_instance = UpdateSchoolGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSchoolGroupRequest.to_json())

# convert the object into a dict
update_school_group_request_dict = update_school_group_request_instance.to_dict()
# create an instance of UpdateSchoolGroupRequest from a dict
update_school_group_request_from_dict = UpdateSchoolGroupRequest.from_dict(update_school_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


