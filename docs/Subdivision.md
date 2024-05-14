# Subdivision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**division_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.subdivision import Subdivision

# TODO update the JSON string below
json = "{}"
# create an instance of Subdivision from a JSON string
subdivision_instance = Subdivision.from_json(json)
# print the JSON string representation of the object
print(Subdivision.to_json())

# convert the object into a dict
subdivision_dict = subdivision_instance.to_dict()
# create an instance of Subdivision from a dict
subdivision_form_dict = subdivision.from_dict(subdivision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


