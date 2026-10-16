# AdminRiNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**requested_item_id** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_ri_note import AdminRiNote

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRiNote from a JSON string
admin_ri_note_instance = AdminRiNote.from_json(json)
# print the JSON string representation of the object
print(AdminRiNote.to_json())

# convert the object into a dict
admin_ri_note_dict = admin_ri_note_instance.to_dict()
# create an instance of AdminRiNote from a dict
admin_ri_note_from_dict = AdminRiNote.from_dict(admin_ri_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


