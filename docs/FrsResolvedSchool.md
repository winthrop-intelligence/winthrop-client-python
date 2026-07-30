# FrsResolvedSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**has_filing** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.frs_resolved_school import FrsResolvedSchool

# TODO update the JSON string below
json = "{}"
# create an instance of FrsResolvedSchool from a JSON string
frs_resolved_school_instance = FrsResolvedSchool.from_json(json)
# print the JSON string representation of the object
print(FrsResolvedSchool.to_json())

# convert the object into a dict
frs_resolved_school_dict = frs_resolved_school_instance.to_dict()
# create an instance of FrsResolvedSchool from a dict
frs_resolved_school_from_dict = FrsResolvedSchool.from_dict(frs_resolved_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


