# GadSchoolSummarySchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.gad_school_summary_school import GadSchoolSummarySchool

# TODO update the JSON string below
json = "{}"
# create an instance of GadSchoolSummarySchool from a JSON string
gad_school_summary_school_instance = GadSchoolSummarySchool.from_json(json)
# print the JSON string representation of the object
print(GadSchoolSummarySchool.to_json())

# convert the object into a dict
gad_school_summary_school_dict = gad_school_summary_school_instance.to_dict()
# create an instance of GadSchoolSummarySchool from a dict
gad_school_summary_school_from_dict = GadSchoolSummarySchool.from_dict(gad_school_summary_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


