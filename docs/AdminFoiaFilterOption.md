# AdminFoiaFilterOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**division_id** | **int** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**subdivision_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_filter_option import AdminFoiaFilterOption

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaFilterOption from a JSON string
admin_foia_filter_option_instance = AdminFoiaFilterOption.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaFilterOption.to_json())

# convert the object into a dict
admin_foia_filter_option_dict = admin_foia_filter_option_instance.to_dict()
# create an instance of AdminFoiaFilterOption from a dict
admin_foia_filter_option_from_dict = AdminFoiaFilterOption.from_dict(admin_foia_filter_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


