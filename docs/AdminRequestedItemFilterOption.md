# AdminRequestedItemFilterOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_requested_item_filter_option import AdminRequestedItemFilterOption

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRequestedItemFilterOption from a JSON string
admin_requested_item_filter_option_instance = AdminRequestedItemFilterOption.from_json(json)
# print the JSON string representation of the object
print(AdminRequestedItemFilterOption.to_json())

# convert the object into a dict
admin_requested_item_filter_option_dict = admin_requested_item_filter_option_instance.to_dict()
# create an instance of AdminRequestedItemFilterOption from a dict
admin_requested_item_filter_option_from_dict = AdminRequestedItemFilterOption.from_dict(admin_requested_item_filter_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


