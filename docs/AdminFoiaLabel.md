# AdminFoiaLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_label import AdminFoiaLabel

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaLabel from a JSON string
admin_foia_label_instance = AdminFoiaLabel.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaLabel.to_json())

# convert the object into a dict
admin_foia_label_dict = admin_foia_label_instance.to_dict()
# create an instance of AdminFoiaLabel from a dict
admin_foia_label_from_dict = AdminFoiaLabel.from_dict(admin_foia_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


