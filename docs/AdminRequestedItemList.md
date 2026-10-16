# AdminRequestedItemList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminRequestedItemListMeta**](AdminRequestedItemListMeta.md) |  | [optional] 
**data** | [**List[AdminRequestedItem]**](AdminRequestedItem.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_requested_item_list import AdminRequestedItemList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRequestedItemList from a JSON string
admin_requested_item_list_instance = AdminRequestedItemList.from_json(json)
# print the JSON string representation of the object
print(AdminRequestedItemList.to_json())

# convert the object into a dict
admin_requested_item_list_dict = admin_requested_item_list_instance.to_dict()
# create an instance of AdminRequestedItemList from a dict
admin_requested_item_list_from_dict = AdminRequestedItemList.from_dict(admin_requested_item_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


