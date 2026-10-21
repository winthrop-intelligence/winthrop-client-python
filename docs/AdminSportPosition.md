# AdminSportPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**coach_id** | **int** |  | 
**coach_name** | **str** |  | 
**school_id** | **int** |  | 
**school_name** | **str** |  | 
**year** | **int** |  | 

## Example

```python
from winthrop_client_python.models.admin_sport_position import AdminSportPosition

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSportPosition from a JSON string
admin_sport_position_instance = AdminSportPosition.from_json(json)
# print the JSON string representation of the object
print(AdminSportPosition.to_json())

# convert the object into a dict
admin_sport_position_dict = admin_sport_position_instance.to_dict()
# create an instance of AdminSportPosition from a dict
admin_sport_position_from_dict = AdminSportPosition.from_dict(admin_sport_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


