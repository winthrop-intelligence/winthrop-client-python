# AdminFoiaRequestsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminFoiaRequest]**](AdminFoiaRequest.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_requests_list import AdminFoiaRequestsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestsList from a JSON string
admin_foia_requests_list_instance = AdminFoiaRequestsList.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestsList.to_json())

# convert the object into a dict
admin_foia_requests_list_dict = admin_foia_requests_list_instance.to_dict()
# create an instance of AdminFoiaRequestsList from a dict
admin_foia_requests_list_from_dict = AdminFoiaRequestsList.from_dict(admin_foia_requests_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


