# AdminSchoolName

An alternate/historical name a school is known by (admin namespace)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**school_name** | **str** | The parent school&#39;s display name | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_name import AdminSchoolName

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolName from a JSON string
admin_school_name_instance = AdminSchoolName.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolName.to_json())

# convert the object into a dict
admin_school_name_dict = admin_school_name_instance.to_dict()
# create an instance of AdminSchoolName from a dict
admin_school_name_from_dict = AdminSchoolName.from_dict(admin_school_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


