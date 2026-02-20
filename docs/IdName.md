# IdName

A generic id/name pair used for filter option lists

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.id_name import IdName

# TODO update the JSON string below
json = "{}"
# create an instance of IdName from a JSON string
id_name_instance = IdName.from_json(json)
# print the JSON string representation of the object
print(IdName.to_json())

# convert the object into a dict
id_name_dict = id_name_instance.to_dict()
# create an instance of IdName from a dict
id_name_from_dict = IdName.from_dict(id_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


