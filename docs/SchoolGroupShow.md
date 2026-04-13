# SchoolGroupShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_group_show import SchoolGroupShow

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolGroupShow from a JSON string
school_group_show_instance = SchoolGroupShow.from_json(json)
# print the JSON string representation of the object
print(SchoolGroupShow.to_json())

# convert the object into a dict
school_group_show_dict = school_group_show_instance.to_dict()
# create an instance of SchoolGroupShow from a dict
school_group_show_from_dict = SchoolGroupShow.from_dict(school_group_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


