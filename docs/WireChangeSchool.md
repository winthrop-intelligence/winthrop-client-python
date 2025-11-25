# WireChangeSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**logo_image** | [**Logo**](Logo.md) |  | [optional] 
**external_logo_image** | [**Logo**](Logo.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.wire_change_school import WireChangeSchool

# TODO update the JSON string below
json = "{}"
# create an instance of WireChangeSchool from a JSON string
wire_change_school_instance = WireChangeSchool.from_json(json)
# print the JSON string representation of the object
print(WireChangeSchool.to_json())

# convert the object into a dict
wire_change_school_dict = wire_change_school_instance.to_dict()
# create an instance of WireChangeSchool from a dict
wire_change_school_from_dict = WireChangeSchool.from_dict(wire_change_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


