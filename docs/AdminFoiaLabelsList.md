# AdminFoiaLabelsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminFoiaLabel]**](AdminFoiaLabel.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_labels_list import AdminFoiaLabelsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaLabelsList from a JSON string
admin_foia_labels_list_instance = AdminFoiaLabelsList.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaLabelsList.to_json())

# convert the object into a dict
admin_foia_labels_list_dict = admin_foia_labels_list_instance.to_dict()
# create an instance of AdminFoiaLabelsList from a dict
admin_foia_labels_list_from_dict = AdminFoiaLabelsList.from_dict(admin_foia_labels_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


