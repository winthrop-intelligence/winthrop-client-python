# SchoolNoComp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**coach_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_no_comp import SchoolNoComp

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolNoComp from a JSON string
school_no_comp_instance = SchoolNoComp.from_json(json)
# print the JSON string representation of the object
print(SchoolNoComp.to_json())

# convert the object into a dict
school_no_comp_dict = school_no_comp_instance.to_dict()
# create an instance of SchoolNoComp from a dict
school_no_comp_from_dict = SchoolNoComp.from_dict(school_no_comp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


