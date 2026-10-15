# AdminCompensationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminCompensationListMeta**](AdminCompensationListMeta.md) |  | [optional] 
**data** | [**List[AdminCompensation]**](AdminCompensation.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_compensation_list import AdminCompensationList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCompensationList from a JSON string
admin_compensation_list_instance = AdminCompensationList.from_json(json)
# print the JSON string representation of the object
print(AdminCompensationList.to_json())

# convert the object into a dict
admin_compensation_list_dict = admin_compensation_list_instance.to_dict()
# create an instance of AdminCompensationList from a dict
admin_compensation_list_from_dict = AdminCompensationList.from_dict(admin_compensation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


