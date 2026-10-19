# UpdateAdminFoiaLabelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_label** | [**UpdateAdminFoiaLabelRequestFoiaLabel**](UpdateAdminFoiaLabelRequestFoiaLabel.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_foia_label_request import UpdateAdminFoiaLabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminFoiaLabelRequest from a JSON string
update_admin_foia_label_request_instance = UpdateAdminFoiaLabelRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminFoiaLabelRequest.to_json())

# convert the object into a dict
update_admin_foia_label_request_dict = update_admin_foia_label_request_instance.to_dict()
# create an instance of UpdateAdminFoiaLabelRequest from a dict
update_admin_foia_label_request_from_dict = UpdateAdminFoiaLabelRequest.from_dict(update_admin_foia_label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


