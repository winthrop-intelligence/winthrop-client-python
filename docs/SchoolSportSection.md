# SchoolSportSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**average_attendance** | **float** |  | [optional] 
**pays_average_cents** | **int** |  | [optional] 
**receives_average_cents** | **int** |  | [optional] 
**seasons** | [**List[SchoolSportSeason]**](SchoolSportSeason.md) |  | [optional] 
**wl_chart** | [**List[SchoolWLChartPoint]**](SchoolWLChartPoint.md) |  | [optional] 
**home_contracts** | [**List[SchoolContractEntry]**](SchoolContractEntry.md) |  | [optional] 
**away_contracts** | [**List[SchoolContractEntry]**](SchoolContractEntry.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_sport_section import SchoolSportSection

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolSportSection from a JSON string
school_sport_section_instance = SchoolSportSection.from_json(json)
# print the JSON string representation of the object
print(SchoolSportSection.to_json())

# convert the object into a dict
school_sport_section_dict = school_sport_section_instance.to_dict()
# create an instance of SchoolSportSection from a dict
school_sport_section_from_dict = SchoolSportSection.from_dict(school_sport_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


