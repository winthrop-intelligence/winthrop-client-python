# AdminFoiaRequestCoachesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminFoiaRequestCoach]**](AdminFoiaRequestCoach.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_coaches_list import AdminFoiaRequestCoachesList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestCoachesList from a JSON string
admin_foia_request_coaches_list_instance = AdminFoiaRequestCoachesList.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestCoachesList.to_json())

# convert the object into a dict
admin_foia_request_coaches_list_dict = admin_foia_request_coaches_list_instance.to_dict()
# create an instance of AdminFoiaRequestCoachesList from a dict
admin_foia_request_coaches_list_from_dict = AdminFoiaRequestCoachesList.from_dict(admin_foia_request_coaches_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


