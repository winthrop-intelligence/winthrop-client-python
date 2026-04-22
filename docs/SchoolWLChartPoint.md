# SchoolWLChartPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**losses** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_wl_chart_point import SchoolWLChartPoint

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolWLChartPoint from a JSON string
school_wl_chart_point_instance = SchoolWLChartPoint.from_json(json)
# print the JSON string representation of the object
print(SchoolWLChartPoint.to_json())

# convert the object into a dict
school_wl_chart_point_dict = school_wl_chart_point_instance.to_dict()
# create an instance of SchoolWLChartPoint from a dict
school_wl_chart_point_from_dict = SchoolWLChartPoint.from_dict(school_wl_chart_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


