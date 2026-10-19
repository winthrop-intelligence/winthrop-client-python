# CreateAdminFoiaLabelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_label** | [**CreateAdminFoiaLabelRequestFoiaLabel**](CreateAdminFoiaLabelRequestFoiaLabel.md) |  | 

## Example

```python
from winthrop_client_python.models.create_admin_foia_label_request import CreateAdminFoiaLabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminFoiaLabelRequest from a JSON string
create_admin_foia_label_request_instance = CreateAdminFoiaLabelRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminFoiaLabelRequest.to_json())

# convert the object into a dict
create_admin_foia_label_request_dict = create_admin_foia_label_request_instance.to_dict()
# create an instance of CreateAdminFoiaLabelRequest from a dict
create_admin_foia_label_request_from_dict = CreateAdminFoiaLabelRequest.from_dict(create_admin_foia_label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


