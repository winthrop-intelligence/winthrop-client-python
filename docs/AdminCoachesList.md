# AdminCoachesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminCoach]**](AdminCoach.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coaches_list import AdminCoachesList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachesList from a JSON string
admin_coaches_list_instance = AdminCoachesList.from_json(json)
# print the JSON string representation of the object
print(AdminCoachesList.to_json())

# convert the object into a dict
admin_coaches_list_dict = admin_coaches_list_instance.to_dict()
# create an instance of AdminCoachesList from a dict
admin_coaches_list_from_dict = AdminCoachesList.from_dict(admin_coaches_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


