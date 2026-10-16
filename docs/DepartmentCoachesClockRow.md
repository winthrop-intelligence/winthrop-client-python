# DepartmentCoachesClockRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_abbrev** | **str** |  | 
**group** | **str** |  | 
**names** | **List[str]** |  | 
**people** | [**List[DepartmentCoachesClockRowPeopleInner]**](DepartmentCoachesClockRowPeopleInner.md) |  | 
**state** | **str** | Where a still-running deal sits against the horizon. &#x60;expires&#x60; is kept for multi-year deals (a term of 13 months or more) ending inside it; a shorter term reads &#x60;single_year&#x60; whenever it ends. A contract whose end date is already behind today never produces a row, and neither does a seat with no contract on file. | 
**var_date** | **str** | The contract&#39;s end date. Never earlier than today. Null only for &#x60;at_will&#x60;, which has no term to run out. | 
**approximate** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.department_coaches_clock_row import DepartmentCoachesClockRow

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachesClockRow from a JSON string
department_coaches_clock_row_instance = DepartmentCoachesClockRow.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachesClockRow.to_json())

# convert the object into a dict
department_coaches_clock_row_dict = department_coaches_clock_row_instance.to_dict()
# create an instance of DepartmentCoachesClockRow from a dict
department_coaches_clock_row_from_dict = DepartmentCoachesClockRow.from_dict(department_coaches_clock_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


