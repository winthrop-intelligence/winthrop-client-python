# CoachCompensationTabQuartilesRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | [optional] 
**percent_rank** | **int** |  | [optional] 
**q25_cents** | **int** |  | 
**q50_cents** | **int** |  | 
**q75_cents** | **int** |  | 
**q100_cents** | **int** |  | 

## Example

```python
from winthrop_client_python.models.coach_compensation_tab_quartiles_rows_inner import CoachCompensationTabQuartilesRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensationTabQuartilesRowsInner from a JSON string
coach_compensation_tab_quartiles_rows_inner_instance = CoachCompensationTabQuartilesRowsInner.from_json(json)
# print the JSON string representation of the object
print(CoachCompensationTabQuartilesRowsInner.to_json())

# convert the object into a dict
coach_compensation_tab_quartiles_rows_inner_dict = coach_compensation_tab_quartiles_rows_inner_instance.to_dict()
# create an instance of CoachCompensationTabQuartilesRowsInner from a dict
coach_compensation_tab_quartiles_rows_inner_from_dict = CoachCompensationTabQuartilesRowsInner.from_dict(coach_compensation_tab_quartiles_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


